from .models import *
from rest_framework import serializers

class StudentData(serializers.Serializer):
    class Meta:
        model = Details
        field = ['Name','Reg_no','mobile_no']