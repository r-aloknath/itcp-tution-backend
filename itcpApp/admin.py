from django.contrib import admin
from .models import StudentAlumni
# Register your models here.
@admin.register(StudentAlumni)
class StudentAdmin(admin.ModelAdmin):
    list_display=['slNo','name','mobile','position','remarks','eMail']