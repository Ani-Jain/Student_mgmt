from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=10,unique=True) 
    school = models.ForeignKey("School",on_delete=models.CASCADE, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 