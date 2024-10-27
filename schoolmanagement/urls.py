
from django.contrib import admin
from django.urls import path, include
from school import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('school.urls'))
    ]