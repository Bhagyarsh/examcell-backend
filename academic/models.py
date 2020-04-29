from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class klass(models.Model):
    classid = models.CharField(unique=True,max_length=16)
    classname = models.CharField(max_length=250)
    startingdate = models.DateField()
    endingdate = models.DateField()

    def __str__(self):
        return self.classname




class student(models.Model):
    clgregisterid = models.CharField(max_length=16)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    enrolledclass = models.OneToOneField(to=klass, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    div = models.CharField(max_length=10)
    phone_no = models.IntegerField()
    email_id = models.EmailField()
    DOB = models.DateField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=16)
    pincode = models.IntegerField()

    def __str__(self):
        return self.classname + " " + self.div

class ktclass(models.Model):
    classname = models.CharField(max_length=250,unique=True)
    classid = models.CharField(max_length=16)
    student = models.OneToOneField(to=student,on_delete=models.CASCADE)
    def __str__(self):
        return self.classname + " " + self.classid


class collegestaff(models.Model):
    clgregisterid = models.CharField(max_length=16)
    designation = models.CharField(max_length=16)
    department = models.CharField(max_length=16)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    email_id = models.EmailField()
    DOB = models.DateField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=16)
    pincode = models.IntegerField()

    def __str__(self):
        return self.user.username + " " + self.department + " " + self.department


class staffprofileeditrequest(models.Model):
    clgregisterid = models.CharField(max_length=16)
    designation = models.CharField(max_length=16)
    department = models.CharField(max_length=16)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone_no = models.IntegerField()
    email_id = models.EmailField()
    DOB = models.DateField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=16)
    pincode = models.IntegerField()

    def __str__(self):
        return self.classname + " " + self.div


class studenteditprofilerequest(models.Model):
    clgregisterid = models.CharField(max_length=16)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    enrolledclass = models.OneToOneField(to=klass, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    div = models.CharField(max_length=10)
    phone_no = models.IntegerField()
    email_id = models.EmailField()
    DOB = models.DateField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=16)
    pincode = models.IntegerField()

    def __str__(self):
        return self.classname + " " + self.div
