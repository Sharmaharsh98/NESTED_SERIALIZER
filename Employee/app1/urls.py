from django.urls import path
from .views import *

urlpatterns = [
    path('emp/', EmployeeDetails.as_view()),
    path('empinfo/<int:regid>/', EmployeeInfo.as_view()),
    path('ad/', Address.as_view(), name='address'),
    path('work/', WorkExperience.as_view(), name= 'work'),
    path('qual/', QualificationInfo.as_view(), name = 'qualification'),
    path('pro/', ProjectInfo.as_view(), name = 'project'),


]