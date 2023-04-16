from django.contrib import admin
from .models import *
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['regid', 'name', 'email', 'age', 'gender', 'phoneNo', 'photo']

admin.site.register(Employee, EmployeeAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['hno', 'street', 'city', 'state']

admin.site.register(AddressDetails, AddressAdmin)


class WorkAdmin(admin.ModelAdmin):
    list_display = ['companyName', 'fromDate', 'toDate', 'address']

admin.site.register(WorkExperience, WorkAdmin)

class QualiAdmin(admin.ModelAdmin):
    list_display = ['qualificationName', 'fromDate', 'toDate', 'percentage']

admin.site.register(Qualifications, QualiAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(Projects, ProjectAdmin)