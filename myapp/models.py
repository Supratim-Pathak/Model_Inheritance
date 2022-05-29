from pyexpat import model
from django.db import models

# Create your models here.

class common_info(models.Model):
    department = models.CharField(max_length=150,null=True)
    
    class Meta:
        abstract= True

class student(common_info):
    stu_name    = models.CharField(max_length=150,null=True)
    stu_roll    = models.BigIntegerField(null=True)
    created_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now_add=True)
    
class teacher(common_info):
    emp_name    = models.CharField(max_length=150, null=True)
    emp_id      = models.BigIntegerField(null=True)
    created_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

class admin_staff(common_info):
    emp_name = models.CharField(max_length=150, null=True)
    emp_id = models.BigIntegerField(null=True)
    department = None
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
   
class exam_center(models.Model):  
    city    = models.CharField(max_length=150)
    landmark= models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class school_of_exam(exam_center):
    school_name  = models.CharField(max_length=150)
    school_created_at = models.DateTimeField(auto_now=True)
    school_updated_at = models.DateTimeField(auto_now_add=True)

    