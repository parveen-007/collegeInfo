"""
URL configuration for collegeinfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teacherinfo.views import landingpage,login,register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landingpage,name='landingpage'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]
# from teacherinfo.views import home,register

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/',home,name='name'),
#     path('register/',register, name='register'),
# >>>>>>> 898b9e21d85f2b274acce3be017d74dd919fa57a

# from teacherinfo.views import home, login

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/',home,name='name'),
#     path('login/',login,name='login'),
# >>>>>>> origin/login

