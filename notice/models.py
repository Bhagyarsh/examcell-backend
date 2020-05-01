from django.db import models
from accounts.utlis import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# Create your models here.
class notice(models.Model):
    slug = models.SlugField(unique=True,blank=True,null=True)
    user = models.ForeignKey(to="academic.collegestaff",on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    added_at = models.DateField(auto_now_add=True)
    uploadedatetime = models.DateTimeField(auto_now_add=True)
    displaytill = models.DateField()
    noticeText = models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    displaytoall = models.BooleanField(default=False)
    displaytoclasses = models.ManyToManyField(to="academic.klass",blank=True)
    displaytoparents = models.BooleanField(default=False)

    def __str__(self):
        return self.title

@receiver(pre_save, sender=notice)
def add_slug_to_Verified_Email_obj(sender, instance, **kwargs):
    if not instance.slug :
        instance.slug = unique_slug_generator(instance)