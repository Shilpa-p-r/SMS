from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test





#Home view
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'school/index.html')




def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'school/adminclick.html')


def staffclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'school/staffclick.html')



def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'school/studentclick.html')


#check group for admin,staff and student
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def is_staff(user):
    return user.groups.filter(name='TEACHER').exists()
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_staff(request.user):
        accountapproval=models.Officestaff.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('staff-dashboard')
        else:
            return render(request,'school/staff_wait_for_approval.html')
    elif is_student(request.user):
        accountapproval=models.Librarian.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('student-dashboard')
        else:
            return render(request,'school/student_wait_for_approval.html')
    else:
        # This final else ensures an HttpResponse is always returned.
        return HttpResponse("Unauthorized access or user role not recognized.", status=403)

#-------------------------------------------------dashboard----------------------------------------------------#
#dashboard view of admin,studentand staff
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    staffcount=models.Officestaff.objects.all().filter(status=True).count()
    librariancount = models.Librarian.objects.all().filter(status=True).count()
    studentcount=models.Students.objects.all().filter(status=True).count()
    staffsalary=models.Officestaff.objects.filter(status=True).aggregate(Sum('salary'))
    studentfee=models.Students.objects.filter(status=True).aggregate(Sum('student_fees',default=0))

    mydict={
        'staffcount':staffcount,
        'librariancount': librariancount,
        'studentcount':studentcount,
        'staffsalary':staffsalary['salary__sum'],
       'studentfee':studentfee['student_fees__sum'],

    }
    return render(request,'school/admin_dashboard.html',context=mydict)


@login_required(login_url='teacherlogin')
@user_passes_test(is_staff)
def staff_dashboard_view(request):
    staffcount=models.Officestaff.objects.all().filter(status=True).count()
    librariancount = models.Librarian.objects.all().filter(status=True).count()
    studentcount=models.Students.objects.all().filter(status=True).count()
    staffsalary=models.Officestaff.objects.filter(status=True).aggregate(Sum('salary'))
    studentfee=models.Students.objects.filter(status=True).aggregate(Sum('fee',default=0))

    mydict={
        'staffcount':staffcount,
        'librariancount': librariancount,
        'studentcount':studentcount,
        'staffsalary':staffsalary['salary__sum'],
        'studentfee':studentfee['fee__sum'],
    }
    return render(request,'school/staff_dashboard.html',context=mydict)


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    staffcount=models.Officestaff.objects.all().filter(status=True).count()
    librariancount = models.Librarian.objects.all().filter(status=True).count()
    studentcount=models.Librarian.objects.all().filter(status=True).count()
    studentfee=models.Librarian.objects.filter(status=True).aggregate(Sum('fee',default=0))

    mydict={
        'staffcount':staffcount,
        'librariancount': librariancount,
        'studentcount':studentcount,
        'studentfee':studentfee['fee__sum'],
  }
    return render(request,'school/student_dashboard.html',context=mydict)

#dashboard of staff and libraian
@login_required(login_url='stafflogin')
@user_passes_test(is_staff)
def staff_dashboard_view(request):
    staffdata=models.Officestaff.objects.all().filter(status=True,user_id=request.user.id)

    mydict={
        'salary':staffdata[0].salary,
        'mobile':staffdata[0].mobile,
        'date':staffdata[0].joindate,

    }
    return render(request,'school/staff_dashboard.html',context=mydict)


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    studentdata=models.Librarian.objects.all().filter(status=True,user_id=request.user.id)

    mydict = {
        'salary': studentdata[0].salary,
        'mobile': studentdata[0].mobile,
        'date': studentdata[0].joindate,

    }
    return render(request,'school/student_dashboard.html',context=mydict)


#staff view from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_staff_view(request):
    return render(request,'school/admin_staff.html')

#librarian view from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_librarian_view(request):
    return render(request,'school/admin_librarian.html')

#satff view from librarian account
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_staff_view(request):
    return render(request,'school/student_staff.html')

#libraraian view from staff account
@login_required(login_url='teacherlogin')
@user_passes_test(is_staff)
def staff_librarian_view(request):
    return render(request,'school/staff_librarian.html')

#---------------------------------------------------------Admin Add -----------------------------------------------------------#
#admin add staff
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_staff_view(request):
    form1=forms.OfficeUserForm()
    form2=forms.OfficestaffForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.OfficeUserForm(request.POST)
        form2=forms.OfficestaffForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_teacher_group = Group.objects.get_or_create(name='staff')
            my_teacher_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-staff')
    return render(request,'school/admin_add_staff.html',context=mydict)

#admin add librarian
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_librarian_view(request):
    form1=forms.LibraUserForm()
    form2=forms.LibrarianForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.LibraUserForm(request.POST)
        form2=forms.LibrarianForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_teacher_group = Group.objects.get_or_create(name='STUDENT')
            my_teacher_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-librarian')
    return render(request,'school/admin_add_librarian.html',context=mydict)

#admin add students
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_student_view(request):
    form1=forms.StudentUserForm()
    form2=forms.StudentsForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        else:
            print("form is invalid")
        return HttpResponseRedirect('admin-student')
    return render(request,'school/admin_add_student.html',context=mydict)

#admin view staff member
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_staff_view(request):
    staff=models.Officestaff.objects.all().filter(status=True)
    return render(request,'school/admin_view_staff.html',{'staff':staff})

#librarian view staff member
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_view_staff_view(request):
    staff=models.Officestaff.objects.all().filter(status=True)
    return render(request,'school/student_view_staff.html',{'staff':staff})

#admin view librarian member
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_librarian_view(request):
    staff=models.Librarian.objects.all().filter(status=True)
    return render(request,'school/admin_view_librarian.html',{'staff':staff})

#staff view librarian member
@login_required(login_url='stafflogin')
@user_passes_test(is_staff)
def staff_view_librarian_view(request):
    staff=models.Librarian.objects.all().filter(status=True)
    return render(request,'school/staff_view_librarian.html',{'staff':staff})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_staff_view(request):
    staff=models.Officestaff.objects.all().filter(status=False)
    return render(request,'school/admin_approve_staff.html',{'teachers':staff})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_staffview(request,pk):
    staff=models.Officestaff.objects.get(id=pk)
    staff.status=True
    staff.save()
    return redirect(reverse('admin-approve-staff'))

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_student_view(request):
    students=models.Students.objects.all().filter(status=False)
    return render(request,'school/admin_approve_student.html',{'students':students})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_student_view(request,pk):
    students=models.Students.objects.get(id=pk)
    students.status=True
    students.save()
    return redirect(reverse('admin-approve-student'))

#---------------------------------------------------update----------------------------------------------------#
#change student detils from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_student_view1(request,pk):
    student=models.Students.objects.get(id=pk)
    user = student.user
    form1=forms.StudentUserForm(instance=user)
    form2=forms.StudentsForm(instance=student)
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST,instance=user)
        form2=forms.StudentsForm(request.POST,instance=student)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('admin-view-student')
    return render(request,'school/admin_update_student.html',context=mydict)

#change staff details from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_staff_view(request,pk):
    staff=models.Officestaff.objects.get(id=pk)
    user=models.User.objects.get(id=staff.user_id)

    form1=forms.OfficeUserForm(instance=user)
    form2=forms.OfficestaffForm(instance=staff)
    mydict={'form1':form1,'form2':form2}

    if request.method=='POST':
        form1=forms.OfficeUserForm(request.POST,instance=user)
        form2=forms.OfficestaffForm(request.POST,instance=staff)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('admin-view-staff')
    return render(request,'school/admin_update_staff.html',context=mydict)

#change librarian details from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_librarian_view(request,pk):
    librarian=models.Librarian.objects.get(id=pk)
    user=models.User.objects.get(id=librarian.user_id)

    form1=forms.LibraUserForm(instance=user)
    form2=forms.LibrarianForm(instance=librarian)
    mydict={'form1':form1,'form2':form2}

    if request.method=='POST':
        form1=forms.LibraUserForm(request.POST,instance=user)
        form2=forms.LibrarianForm(request.POST,instance=librarian)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('admin-view-librarian')
    return render(request,'school/admin_update_libraian.html',context=mydict)

#Update view of student from staff
@login_required(login_url='stafflogin')
@user_passes_test(is_staff)
def update_student_view2(request,pk):
    student=models.Students.objects.get(id=pk)
    user = student.user
    form1=forms.StudentUserForm(instance=user)
    form2=forms.StudentsForm(instance=student)
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST,instance=user)
        form2=forms.StudentsForm(request.POST,instance=student)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('staff-view-student')
    return render(request,'school/staff_update_student.html',context=mydict)

#update view of student from librarian
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def update_student_view3(request,pk):
    student=models.Students.objects.get(id=pk)
    user = student.user
    form1=forms.StudentUserForm(instance=user)
    form2=forms.StudentsForm(instance=student)
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST,instance=user)
        form2=forms.StudentsForm(request.POST,instance=student)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('student-view-student')
    return render(request,'school/admin_update_student.html',context=mydict)

#------------------------------------------------salary view-------------------------------------------------#
#salary view of staff from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_staff_salary_view(request):
    staff=models.Officestaff.objects.all()
    return render(request,'school/admin_view_staff_salary.html',{'staff':staff})

#salary view of staff from librarian account
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_view_staff_salary_view(request):
    staff=models.Officestaff.objects.all()
    return render(request,'school/student_view_staff_salary.html',{'staff':staff})

#salary view of librarian from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_librarian_salary_view(request):
    staff=models.Librarian.objects.all()
    return render(request,'school/admin_view_librarian_salary.html',{'staff':staff})

#salary view of librarian from staff account
@login_required(login_url='stafflogin')
@user_passes_test(is_staff)
def staff_view_librarian_salary_view(request):
    staff=models.Librarian.objects.all()
    return render(request,'school/staff_view_librarian_salary.html',{'staff':staff})

#------------------------student view----------------------------#
#student view from admin
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_student_view(request):
    return render(request,'school/admin_student.html')

#student view from staff
@login_required(login_url='stafflogin')
@user_passes_test(is_staff)
def staff_student_view(request):
    return render(request,'school/staff_student.html')

#student view from librarian
@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_student_view(request):
    return render(request,'school/student_student.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_student_view(request):
    students=models.Students.objects.all().filter(status=True)
    return render(request,'school/admin_view_student.html',{'students':students})


@login_required(login_url='stafflogin')
@user_passes_test(is_staff)
def staff_view_student_view(request):
    students=models.Students.objects.all().filter(status=True)
    return render(request,'school/staff_view_student.html',{'students':students})


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_view_student_view(request):
    students=models.Students.objects.all().filter(status=True)
    return render(request,'school/student_view_student.html',{'students':students})

#------------------------------------delete ----------------------------------------#
@login_required(login_url='stafflogin')
@user_passes_test(is_staff)
def delete_staff_from_school_view(request,pk):
    student=models.Officestaff.objects.get(id=pk)
    user=student.user
    user.delete()
    student.delete()
    return redirect('admin-view-staff')


#delete librarian from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_librarian_from_school_view(request,pk):
    librarian=models.Librarian.objects.get(id=pk)
    user=models.User.objects.get(id=librarian.user_id)
    user.delete()
    librarian.delete()
    return redirect('admin-view-librarian')

#delete staff from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_staff_from_school_view(request,pk):
    staff=models.Officestaff.objects.get(id=pk)
    user=models.User.objects.get(id=staff.user_id)
    user.delete()
    staff.delete()
    return redirect('admin-view-staff')

#Delete  student from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_student_from_school_view(request,pk):
    student=models.Students.objects.get(id=pk)
    user=student.user
    user.delete()
    student.delete()
    return redirect('admin-view-student')

#delete staff,student,and librarian from admin account
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_student_view(request,pk):
    student=models.Students.objects.get(id=pk)
    user=student.user
    user.delete()
    student.delete()
    return redirect('admin-approve-student')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_staff_view(request,pk):
    student=models.Students.objects.get(id=pk)
    user=student.user
    user.delete()
    student.delete()
    return redirect('admin-approve-staff')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_librarian_view(request,pk):
    librarian=models.Librarian.objects.get(id=pk)
    user=models.User.objects.get(id=librarian.user_id)
    user.delete()
    librarian.delete()
    return redirect('admin-approve-student')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_staff_from_school_view(request,pk):
    staff=models.Officestaff.objects.get(id=pk)
    user=models.User.objects.get(id=staff.user_id)
    user.delete()
    staff.delete()
    return redirect('admin-view-staff')



















