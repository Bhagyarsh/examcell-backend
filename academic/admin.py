from django.contrib import admin
from .models import student,collegestaff,ktclass,klass,staffprofileeditrequest,studenteditprofilerequest,collegestaff
# Register your models here.
admin.site.register(student)
admin.site.register(klass)
admin.site.register(ktclass)
admin.site.register(collegestaff)
admin.site.register(staffprofileeditrequest)
admin.site.register(studenteditprofilerequest)
