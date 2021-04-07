from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crm_automation.models import Course,Batch,Enquiry,Registration,Feepayment
from datetime import date
class Registrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
class Loginform(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=100)
class courseform(ModelForm):
    class Meta:
        model=Course
        fields="__all__"
class Batchform(ModelForm):
    class Meta:
        model=Batch
        fields="__all__"
        widgets = {
            'starting_date': forms.DateInput(format=('%m/%d/%Y'),
                                    attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                           'type': 'date'}),
        }
class Studentform(ModelForm):
    class Meta:
        model=Enquiry
        fields=['enquiry_id','student_name','address','qualification','collegename','course','phone','email','batch_code','followupdate','admission_status']
        widgets = {
            'followupdate': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                       'type': 'date'}),
        }

class Admissionform(ModelForm):
    class Meta:
        model=Registration
        fields="__all__"
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'),
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                   'type': 'date'}),
        }
class Paymentform(ModelForm):
    class Meta:
        model=Feepayment
        fields="__all__"
        widgets = {
            'payment_date': forms.DateInput(format=('%m/%d/%Y'),
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                   'type': 'date'}),
        }
