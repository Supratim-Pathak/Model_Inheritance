from django.contrib import admin
from myapp.models import *
# Register your models here.

@admin.register(student)
class student_admin(admin.ModelAdmin):
    list_display =['id', 'department', 'stu_name', 'stu_roll', 'created_at', 'updated_at']

@admin.register(teacher)
class teacher_admin(admin.ModelAdmin):
    list_display =['id', 'department', 'emp_name', 'emp_id', 'created_at', 'updated_at']

@admin.register(admin_staff)
class admin_staff_admin(admin.ModelAdmin):
    list_display =['id', 'emp_name', 'emp_id', 'created_at', 'updated_at']

@admin.register(exam_center)
class exam_center_admin(admin.ModelAdmin):
    list_display = ['id','city','landmark', 'created_at', 'updated_at']

@admin.register(school_of_exam)
class school_of_exam_admin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'created_at', 'updated_at']
