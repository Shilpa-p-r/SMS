from django import forms
from django.contrib.auth.models import User
from . import models



#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']



class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class StudentsForm(forms.ModelForm):
    class Meta:
        model=models.Students
        fields=['username','roll_no','cl','mobile','book_title','book_borrow_date','return_date','bookdue_date','student_fees','date_paid','pay_duedate','payment_method','remark','status']



class OfficeUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class OfficestaffForm(forms.ModelForm):
    class Meta:
        model=models.Officestaff
        fields=['first_name','salary','mobile','status']


class LibraUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class LibrarianForm(forms.ModelForm):
    class Meta:
        model=models.Librarian
        fields=['first_name','salary','mobile','status']








class AskDateForm(forms.Form):
    date=forms.DateField()







