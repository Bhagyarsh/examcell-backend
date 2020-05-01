from django.db import models
from academic.models import student
# Create your models here.

class Transcript(models.Model):
    student = models.OneToOneField(to=student,on_delete=models.CASCADE)
    added_at = models.DateField(auto_now_add=True)
    reason = models.TextField()
    marksheet12 = models.ImageField(upload_to='static/Trancript/')
    marksheet34 = models.ImageField(upload_to='static/Trancript/')
    marksheet56 = models.ImageField(upload_to='static/Trancript/')
    marksheet78 = models.ImageField(upload_to='static/Trancript/',blank=True,null=True)
    feerecipt = models.ImageField(upload_to='static/Trancript/')
    application =  models.ImageField(upload_to='static/Trancript/')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student.user.username
