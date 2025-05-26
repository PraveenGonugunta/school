from django.db import models

# Create your models here.
class Admission(models.Model):
    std_name=models.CharField(max_length=50)
    std_age=models.IntegerField()
    #def __str__(self):
       # return Admission
    class Meta:
        verbose_name="Admission"
        verbose_name_plural="Admissions"

class Student(models.Model):
    college_name=models.CharField(max_length=50)
    DOJ=models.DateField()
    #def __str__(self):
       # return Admission
    class Meta:
        verbose_name="Student"
        verbose_name_plural="Students"


