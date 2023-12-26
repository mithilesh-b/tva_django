#url mapper 
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name="home"),
    path('about',views.about_page, name="about"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('incourse', views.user_course, name="incourse"),
    path ('', views.viewall, name='viewall'),
    path('admin_tva', views.admin_page, name='admin_tva'),
    path('upload_video/<int:course_id>/', views.upload_video, name='upload_video'),
    path('upload_material/<int:course_id>/', views.upload_material, name='upload_material'),
 ]
