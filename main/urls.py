from django.urls import path,include
from .views import *
urlpatterns = [
    path('<int:i>',index),
    path('create/', create),
    path('',home),
    path('d/',SMSsender),
    path('d/otp/',otpverify),
    path('ad/adder/',Upload),
]