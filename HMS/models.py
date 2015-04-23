from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import hashlib, datetime, random
from datetime import date
from django import forms
from localflavor.us.forms import USStateSelect
from localflavor.us.us_states import US_STATES
from localflavor.us.models import USZipCodeField
from django.utils import timezone
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    SINGLE = 'SIN'
    MARRIED = 'MAR'
    STATUS_CHOICES = ((SINGLE,'Single'),(MARRIED, 'Married'))

    MALE = 'MAL'
    FEMALE = 'FEM'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

    email = models.EmailField(
        verbose_name='e-mail',
        max_length=255,
        unique=True,
        )

    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
    first_name = models.CharField(max_length = 20, default = "")
    last_name = models.CharField(max_length = 20, default = "")
    birth_date = models.DateField(default=date.today()) 
    phone_number = PhoneNumberField(null=True)
    gender = models.CharField(max_length = 7, default = "", choices = GENDER_CHOICES)
    marital_Status = models.CharField(max_length = 10, default = "", choices = STATUS_CHOICES)

    #Address
    house_number = models.IntegerField(default = 0)
    street = models.CharField(max_length = 30, default = "")
    city = models.CharField(max_length = 20, default = "")
    state = models.CharField(max_length = 20, default = "", choices = US_STATES)
    zip_code = USZipCodeField()

    #Emergency Contact
    name = models.CharField(max_length = 50, default = "")
    relation = models.CharField(max_length = 20, default = "")
    primary_Phone = models.IntegerField(default = 0)
    secondary_Phone = models.IntegerField(default = 0)
    is_content_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = ('MyUser')
        verbose_name_plural = ('MyUsers')

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        # if user being demoted from content manager, make sure they are not
        # managing any courses
        super().save(*args, **kwargs)


class Nurse(MyUser):
    PEDIATRICS = 'PED'
    ONCOLOGY = 'ONC'
    FAMILY_PRACTICE = 'FAM'
    EMERGENCY = 'EME'
    ORTHOPEDICS = 'ORT'
    DEPT_CHOICES = ((PEDIATRICS, 'Pediatrics'), 
                    (ONCOLOGY, 'Oncology'), 
                    (FAMILY_PRACTICE, 'Family Practice'), 
                    (EMERGENCY, 'Emergency'), 
                    (ORTHOPEDICS, 'Orthopedics'))
    department = models.CharField(max_length = 30, default = "", choices=DEPT_CHOICES)
    is_nurse = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=True)
   
    class Meta:
        verbose_name = ('Nurse')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.email

class Doctor(MyUser):
    PEDIATRICS = 'PED'
    ONCOLOGY = 'ONC'
    FAMILY_PRACTICE = 'FAM'
    EMERGENCY = 'EME'
    ORTHOPEDICS = 'ORT'
    SPEC_CHOICES = ((PEDIATRICS, 'Pediatrics'), 
                    (ONCOLOGY, 'Oncology'), 
                    (FAMILY_PRACTICE, 'Family Practice'), 
                    (EMERGENCY, 'Emergency'), 
                    (ORTHOPEDICS, 'Orthopedics'))
    MED = 'MD'
    OST = 'DO'

    DEG_CHOICES = ((MED, 'M.D.'), 
                    (OST, 'D.O.'))
    degree = models.CharField(max_length = 40, default = MED, choices = DEG_CHOICES )
    specialty = models.CharField(max_length = 30, default = "", choices=SPEC_CHOICES) #Try to turn into checkbox
    experience = models.CharField(max_length = 60, default = "")
    is_doctor = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = ('Doctor')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.first_name +' '+ self.last_name    
    
class Patient(MyUser):
    PEDIATRICS = 'PED'
    ONCOLOGY = 'ONC'
    FAMILY_PRACTICE = 'FAM'
    EMERGENCY = 'EME'
    ORTHOPEDICS = 'ORT'
    DEPT_CHOICES = ((PEDIATRICS, 'Pediatrics'), 
                    (ONCOLOGY, 'Oncology'), 
                    (FAMILY_PRACTICE, 'Family Practice'), 
                    (EMERGENCY, 'Emergency'), 
                    (ORTHOPEDICS, 'Orthopedics'))
    department = models.CharField(max_length = 30, default = "", choices=DEPT_CHOICES)
    medical_History = models.CharField(max_length = 40, default = "")
    insurance_Provider = models.CharField(max_length = 40, default = "")
    insurance_Policy_Number = models.IntegerField(default = 0)
    is_patient = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=True)
    allergies = models.CharField(max_length = 40, default = "")
    prescriptions = models.CharField(max_length = 40, default = "")
    primaryCareProvider = models.ForeignKey(Doctor, default = 1, blank = True, null = True)

    class Meta:
        verbose_name = ('Patient')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.first_name +' '+self.last_name

class Appointment(models.Model):
    purpose = models.CharField(max_length = 20, default = "")
    startTime = models.DateTimeField(default = timezone.now())
    endTime = models.DateTimeField(default = timezone.now()+datetime.timedelta(hours=1))
    doctor = models.ForeignKey(Doctor, default = 1)
    patient = models.ForeignKey(Patient, default = 1)
    billed = models.BooleanField(default = False)

    def __str__(self):
        return self.patient.last_name + ':' + self.purpose
    
class Bill(models.Model):
    releaseDate = models.DateField(default = datetime.date.today())
    dueDate = models.DateField(default = datetime.date.today() + datetime.timedelta(days = 30))
    amount = models.DecimalField(max_digits=9, decimal_places = 2, default = Decimal('0.00'),
                                 validators = [MinValueValidator(0.0)])
    appointment = models.OneToOneField(Appointment, primary_key = False, null = True)
    patient = models.ForeignKey(Patient, default = 1)
    PAID = "Paid"
    DUE = "Due"
    OVER = "Overdue"
    STATUS_CHOICES = ((DUE, 'Due'),
                      (PAID, 'Paid'),
                      (OVER, 'Overdue'))
    status = models.CharField(max_length = 8, default = "", choices=STATUS_CHOICES)
    released = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.last_name + ':' + str(self.id)
