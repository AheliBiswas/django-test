from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=50,null=False,blank=False)
    lastname=models.CharField(max_length=50,null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    DOB=models.DateField(null=False,blank=False)
    phone_no=models.CharField(max_length=10,blank=False)
    email=models.CharField(max_length=250,null=False,blank=False)

    def __str__(self):
        return (self.firstname)+(self.lastname)
    
class Address(models.Model):
    cutomer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    street_name=models.TextField(max_length=200,null=False,blank=False)
    pincode=models.CharField(max_length=6,null=False,blank=False)
    city=models.CharField(max_length=20,blank=False,null=False)
    state=models.CharField(max_length=20,blank=False,null=False)
    countrycode=models.CharField(max_length=2,null=False,blank=False)

    def __str__(self):
        return self.street_name
    
class Car(models.Model):
    class model_names(models.TextChoices):
        Mercedes_Benz="Mercedes-Benz"     
        Nissan="Nissan"
        Cadillac="Cadillac"
        Volkswagen_Beetle="Volkswagen"
    class manufacturer_names(models.TextChoices):
        The_Mercedes_Benz_Group="Mercedes-Benz"     
        Nissan_Mass_Market_Cars="Nissan"
        Cadillac_Luxury_Vehicles="Cadillac"
        Volkswagen=" Volkswagen"
    class colors(models.TextChoices):
        red="Red"
        blue="Blue"
        green="Green"
        black="Black"

    model_name=models.CharField(max_length=20,choices=model_names.choices,default=None)
    manufacturing_date=models.DateTimeField(auto_now_add=True)
    manufacturer=models.CharField(max_length=20,choices=manufacturer_names.choices,default=None)
    color=models.CharField(max_length=20,choices=colors.choices,default=None)

    def __str__(self):
        return self.model_name
    