from django.db import models

# Create your models here.
class notice(models.Model):
    user = models.ForeignKey(to="academic.collegestaff",on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    uploadedatetime = models.DateTimeField(auto_now_add=True)
    displaytill = models.DateField()
    noticeText = models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    displaytoall = models.BooleanField(default=False)
    displaytoclasses = models.ManyToManyField(to="academic.klass")
    displaytoparents = models.BooleanField(default=False)

    def __str__(self):
        return self.title
