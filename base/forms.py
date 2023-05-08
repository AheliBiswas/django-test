from django.forms import ModelForm
from .models import Customer,Address,Car
from django import forms
from datetime import date

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields =['firstname','lastname','age','DOB','phone_no','email']
        widgets={
            'firstname':forms.TextInput(attrs={'class':'from-control','placeholder':'Enter your first name' ,'id':'firstname_id'}),
            'lastname':forms.TextInput(attrs={'class':'from-control','placeholder':'Enter your last name' , 'id':'lastname_id'}),
            'age':forms.NumberInput(attrs={'class':'from-control', 'placeholder':'Enter your age' ,'id':'age_id','min':'18'}),
            'DOB':forms.DateInput(attrs={'class':'from-control','type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',  'id':'dob_id'}),
            'phone_no':forms.TextInput(attrs={'class':'from-control','placeholder':'Enter your phone number' , 'id':'phoneno_id'}),
            'email':forms.EmailInput(attrs={'class':'from-control','placeholder':'Enter your email id' , 'id':'email_id'})
        }

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'