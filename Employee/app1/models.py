from django.db import models

# Create your models here.

GENDER_CHOICES =[('Male', 'Male'), ('Female', 'Female'), ( 'Other', 'Other')]


class Employee(models.Model):
    regid = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique= True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    phoneNo = models.CharField(max_length=12)
    photo = models.ImageField(upload_to="Employee_Picture", null=True)

    def __str__(self):
        	return f"{self.regid}"
         
class AddressDetails(models.Model):
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE, related_name= 'Address')
    hno = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    
class WorkExperience(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Experience')
    companyName = models.CharField(max_length=50)
    fromDate = models.CharField(max_length=20)
    toDate = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


class Qualifications(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Qualification')
    qualificationName = models.CharField(max_length=50)
    fromDate = models.CharField(max_length=20)
    toDate = models.CharField(max_length=20)
    percentage = models.FloatField()



class Projects(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Project')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=20)



    