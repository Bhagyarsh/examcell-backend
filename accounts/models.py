from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from random import randint
from .utlis import random_string_generator, unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
 
DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)

class UserManager(BaseUserManager):
    def create_user(self,username,  first_name, last_name,  password=None):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, first_name, last_name, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,

        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# hook in the New Manager to our Model


class User(AbstractBaseUser):
    username = models.CharField(max_length=255,unique=True,)
    phone_no = models.IntegerField( blank=True, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=True, null=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    Verified = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return str(self.username)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_verified(self):
        "Is the user a member of staff?"
        return self.Verified

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class Verifiy_email(models.Model):
    email = models.EmailField(null=True,blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    key = models.SlugField(max_length=250, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    Verified_at = models.DateTimeField(auto_now=True)
    Verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class UserEmailUpdate(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    last_email = models.EmailField(blank=True, null=True)
    update_start_on = models.DateTimeField(auto_now_add=True)    
    updated = models.BooleanField(default=False,blank=True, null=True)

    def __str__(self):
        return self.last_email   
    
STAFF_CHOICES = (
    ("ADMIN", ("Admin")),
    ("ACADEMIC", ("Academic Dept.")),
    ("EXAM CELL", ("Exam cell")),
)
class User_update(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    key = models.SlugField(max_length=250, null=True, blank=True)
    filed = models.CharField(max_length=250, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Verified = models.BooleanField(default=False)

class profile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    dp = models.ImageField(blank=True,null=True)
    college_staff = models.BooleanField(default=False)
    student = models.BooleanField(default=True)
    parents = models.BooleanField(default=False)
    ifstaffrole = models.CharField(max_length = 20, 
        choices = STAFF_CHOICES,null=True,blank=True )

    def __str__(self):
        return self.user.username

@receiver(pre_save, sender=UserEmailUpdate)
def if_email_add_Verified_Email_obj(sender, instance, **kwargs):
    if not instance.last_email:
        instance.last_email = instance.user.email
    if instance.user:
        Verifiy_email.objects.create(user=instance,email=instance.email)


@receiver(post_save, sender=User)
def if_email_add_Verified_Email_obj(sender, instance, created, **kwargs):
    if created:
        if instance.email:
            Verifiy_email.objects.create(user=instance,email=instance.email)


@receiver(pre_save, sender=Verifiy_email)
def add_slug_to_Verified_Email_obj(sender, instance, **kwargs):
    if not instance.slug and not instance.key:
        instance.slug = unique_slug_generator(instance)
        instance.key = unique_slug_generator(instance)

    if instance.Verified:
        instance.user.Verified = True
        instance.user.save()


@receiver(pre_save, sender=User)
def if_email_add_Verified_Email_obj(sender, instance, **kwargs):
    if instance.username:
        if not instance.email or not instance.phone_no:
            if "@" in  instance.username:
                instance.email = instance.username
            if len(instance.username) == 10 and (instance.username.isdigit()):
                instance.phone_no =  instance.username




