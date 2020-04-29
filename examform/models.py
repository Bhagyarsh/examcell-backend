from django.db import models
from academic.models import collegestaff,klass
# Create your models here.
class examform(models.Model):
    klass = models.ForeignKey(to=klass,on_delete=models.CASCADE)
    sem = models.CharField(max_length=2)
    added_on = models.DateTimeField(auto_now_add=True)
    open_till = models.DateField()
    addedby = models.ForeignKey(to=collegestaff,on_delete=models.CASCADE)
    is_kt = models.BooleanField(default=False)
    pervioushalltickit_no = models.CharField(max_length=16)
    feerecipt = models.ImageField()
    fee = models.IntegerField()

    def __str__(self):
        return self.klass + " " +  self.sem
