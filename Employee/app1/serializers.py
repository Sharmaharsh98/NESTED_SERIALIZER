from .models import Employee, AddressDetails, WorkExperience, Projects , Qualifications
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    hno = serializers.CharField(max_length=10)
    street = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    class Meta:
        model = AddressDetails
        fields = ['id', 'hno', 'street', 'city', 'state']


class WorkExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkExperience
        fields = ['id', 'companyName', 'fromDate', 'toDate', 'address']


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualifications
        fields = ['id', 'qualificationName', 'fromDate', 'toDate', 'percentage']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description']


class EmployeeSerializer(serializers.ModelSerializer):
    Address = AddressSerializer()
    Experience = WorkExperienceSerializer(many = True)
    Qualification = QualificationSerializer(many = True)
    Project = ProjectSerializer(many = True)

    def create(self, validated_data):
        Add = validated_data.pop('Address')
        Exp = validated_data.pop('Experience')
        Qua = validated_data.pop('Qualification')
        Proj = validated_data.pop('Project')

        employee = Employee.objects.create(**validated_data)
        ###############One to One################################
        AddressDetails.objects.create(employee = employee, **Add)
        ###############Foreign###################################
        for i in Exp:
            WorkExperience.objects.create(**i, employee = employee)
        ##########################################################
        for i in Qua:
            Qualifications.objects.create(**i, employee = employee)
        ##########################################################
        for i in Proj:
                Projects.objects.create(**i, employee = employee)

        return employee
    

    class Meta:
        model = Employee
        fields = ['regid', 'name', 'email', 'age', 'gender', 'phoneNo', 'photo', 'Address', 'Experience', 'Qualification', 'Project']





