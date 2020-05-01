from django.db import models
from academic.models import collegestaff,klass,ktclass,student
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from accounts.utlis import unique_slug_generator

class examform(models.Model):
    slug = models.SlugField(unique=True,blank=True,null=True)
    klass = models.ForeignKey(to=klass,on_delete=models.CASCADE,null=True,blank=True)
    ktclass = models.ForeignKey(to=ktclass,on_delete=models.CASCADE,null=True,blank=True)
    sem = models.CharField(max_length=2)
    added_on = models.DateTimeField(auto_now_add=True)
    open_till = models.DateField()
    addedby = models.ForeignKey(to=collegestaff,on_delete=models.CASCADE)
    is_kt = models.BooleanField(default=False)
    fee = models.IntegerField()

    def __str__(self):
        if self.klass != None:
            return self.klass.classname + " " +  self.sem
        else :
            return self.ktclass.classname + " " +  self.sem


class examformFill(models.Model):
    examform = models.ForeignKey(to="examform",on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    pervioushalltickit_no = models.CharField(max_length=16,null=True,blank=True)
    feerecipt = models.ImageField(null=True,blank=True)
    student = models.OneToOneField(to=student,on_delete=models.CASCADE,null=True,blank=True)
    filled = models.BooleanField(default=False)
    def __str__(self):
         return self.student.user.username + " " +  self.examform.sem + " " +  str(self.filled)

@receiver(pre_save, sender=examform)
def add_slug_to_Verified_Email_obj(sender, instance, **kwargs):
    if not instance.slug :
        instance.slug = unique_slug_generator(instance)

