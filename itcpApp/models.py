from django.db import models

# Create your models here.
class StudentAlumni(models.Model):
    slNo=models.IntegerField()
    name=models.CharField(max_length=50)
    mobile=models.IntegerField(primary_key=True)
    position=models.CharField(max_length=100)
    remarks=models.CharField(max_length=400)
    eMail=models.CharField(max_length=50)
    def __str__(self):
        return self.name+" "+str(self.mobile)