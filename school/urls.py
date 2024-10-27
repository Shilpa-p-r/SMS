
from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),          #home


    path('adminclick', views.adminclick_view),
    path('staffclick', views.staffclick_view),
    path('studentclick', views.studentclick_view),


    path('adminlogin', LoginView.as_view(template_name='school/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='school/studentlogin.html')),
    path('stafflogin', LoginView.as_view(template_name='school/stafflogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='school/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('staff-dashboard', views.staff_dashboard_view,name='staff-dashboard'),
    path('student-dashboard', views.student_dashboard_view, name='student-dashboard'),



    path('admin-add-staff', views.admin_add_staff_view,name='admin-add-staff'),
    path('admin-add-librarian', views.admin_add_librarian_view, name='admin-add-librarian'),
    path('admin-add-student', views.admin_add_student_view,name='admin-add-student'),



    path('update-staff/<int:pk>', views.update_staff_view,name='update-staff'),
    path('update-student1/<int:pk>', views.update_student_view1,name='update-student1'),
    path('update-student2/<int:pk>', views.update_student_view2,name='update-student2'),
    path('update-student3/<int:pk>', views.update_student_view3,name='update-student3'),
    path('update-librarian/<int:pk>', views.update_librarian_view, name='update-librarian'),


    path('admin-student', views.admin_student_view,name='admin-student'),
    path('staff-student', views.staff_student_view,name='staff-student'),
    path('student-student', views.student_student_view,name='student-student'),
    path('admin-staff', views.admin_staff_view, name='admin-staff'),
    path('student-staff', views.student_staff_view, name='student-staff'),
    path('admin-librarian', views.admin_librarian_view, name='admin-librarian'),
    path('staff-librarian', views.staff_librarian_view, name='staff-librarian'),



    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('staff-view-student', views.staff_view_student_view,name='staff-view-student'),
    path('student-view-student', views.student_view_student_view,name='student-view-student'),
    path('admin-view-staff-salary', views.admin_view_staff_salary_view, name='admin-view-staff-salary'),
    path('student-view-staff-salary', views.student_view_staff_salary_view, name='student-view-staff-salary'),
    path('admin-view-librarian-salary', views.admin_view_librarian_salary_view, name='admin-view-librarian-salary'),
    path('staff-view-librarian-salary', views.staff_view_librarian_salary_view, name='staff-view-librarian-salary'),
    path('admin-view-staff', views.admin_view_staff_view,name='admin-view-staff'),
    path('student-view-staff', views.student_view_staff_view,name='student-view-staff'),
    path('admin-view-librarian', views.admin_view_librarian_view,name='admin-view-librarian'),
    path('staff-view-librarian', views.staff_view_librarian_view,name='staff-view-librarian'),


    path('delete-librarian-from-school/<int:pk>', views.delete_librarian_from_school_view,name='delete-librarian-from-school'),
    path('delete-librarian/<int:pk>', views.delete_librarian_view,name='delete-librarian'),
    path('delete-student/<int:pk>', views.delete_student_view, name='delete-student'),
    path('delete-staff/<int:pk>', views.delete_staff_view, name='delete-staff'),
    path('delete-staff-from-school/<int:pk>', views.delete_staff_from_school_view, name='delete-staff-from-school'),
    path('delete-student-from-school/<int:pk>', views.delete_student_from_school_view,name='delete-student-from-school')


]
