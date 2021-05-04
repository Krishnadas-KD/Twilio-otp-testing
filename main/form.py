from django import forms

class Createform(forms.Form):
    name =forms.CharField(label="Name",max_length=50)
    regno= forms.IntegerField(label="Reg No",max_value=99999999)
    mobilno=forms.IntegerField(label="Phone No",max_value=9999999999)
    