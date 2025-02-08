from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from multiselectfield import MultiSelectField


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Date Joined", blank=True)
    updated_at = models.DateTimeField(verbose_name="Date Updated", blank=True)
    dob = models.DateField(verbose_name="Date of Birth", null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    phone_number = PhoneNumberField(null=True, blank=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return "{}: {}{}".format(self.username, self.first_name, self.last_name)

    class Meta:
        db_table = "auth_user"

class Student(CustomUser):
    comment = models.CharField(max_length=50, null = True)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


class Teacher(CustomUser):
    comment = models.CharField(max_length=50, null = True)
     
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'



class Group(models.Model):
    group_name = models.CharField(max_length=50, unique=True, blank=False)
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]


    select_days = MultiSelectField(choices=DAY_CHOICES)
    created_date = models.DateTimeField(verbose_name= 'creation_date', blank= True, null = True) 
    students =  models.ManyToManyField(Student, blank = True)