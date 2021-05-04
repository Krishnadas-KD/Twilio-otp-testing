from django.db import models

# Create your models here.

class Details(models.Model):
    Name=models.CharField(max_length=50,unique=False)
    Reg_no=models.IntegerField(unique=False)
    mobile_no=models.IntegerField(unique=False)

