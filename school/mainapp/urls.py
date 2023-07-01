from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('view_all_school',views.all_school, name='all_school'),
    path('add_school',views.add_School, name='add_school'),
    path('remove_school',views.remove_School, name='remove_school'),
    path('filter_school',views.filter_school, name='filter_school'),
    path('remove_school/<int:sch_id>',views.remove_School, name='remove_school'),
    path('update_school',views.update_school, name='update_school'),
    

    path('view_all_student',views.all_student, name='all_student'),
    path('add_student',views.add_student, name='add_student'),
    path('remove_student',views.remove_student, name='remove_student'),
    path('filter_student',views.filter_student, name='filter_student'),
    path('remove_student/<int:stu_id>',views.remove_student, name='remove_student'),
    path('update_student',views.update_student, name='update_student'),
    
]
