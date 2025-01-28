from django.db import models

class  Student(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=True)
    fname = models.CharField( max_length=50)
    lname = models.CharField( max_length=50)
    middle_name = models.CharField( max_length=50, blank = True)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone_num =  models.PhoneNumberField()
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    #     # settings.py
    # USE_TZ = True  # Enables timezone support
    # TIME_ZONE = 'UTC'  # Default time zone for your project
    updated_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fname} + {self.lname}'
    

class Parent(models.Model):
    fname = models.CharField( max_length=50)
    lname = models.CharField( max_length=50)
    phone_num =  models.PhoneNumberField()
    is_staff = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fname} + {self.lname}'




class  Teacher(models.Model):
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    fname = models.CharField( max_length=50)
    lname = models.CharField( max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone_num =  models.PhoneNumberField()
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fname} + {self.lname}'
