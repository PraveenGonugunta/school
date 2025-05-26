from django.contrib import admin
from .models import Admission
from .models import Student


# Register your models here.

class AdmissionAdmin(admin.ModelAdmin):
    list_display=('std_name','std_age')

class StudentAdmin(admin.ModelAdmin):
    list_display=('college_name','DOJ')

admin.site.register(Admission,AdmissionAdmin)
admin.site.register(Student,StudentAdmin)
