from django.db import models
from academic.models import student
# Create your models here.

class Transcript(models.Model):
    student = models.OneToOneField(to=student,on_delete=models.CASCADE)
    reason = models.TextField()
    marksheet12 = models.ImageField()
    marksheet34 = models.ImageField()
    marksheet56 = models.ImageField()
    marksheet78 = models.ImageField(blank=True,null=True)
    feerecipt = models.ImageField()
    application =  models.ImageField()

    def __str__(self):
        return self.student.user.username
