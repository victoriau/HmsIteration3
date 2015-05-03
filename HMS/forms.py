from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from HMS.models import MyUser, Nurse, Doctor, Patient, Appointment, Bill
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms.models import inlineformset_factory
import datetime

class PatientCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            Patient._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(PatientCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class PCPChangeForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('primaryCareProvider',)

class ApptChangeForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('startTime', 'endTime')

class PatientChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Patient
        fields = ('email', 'password', 'first_name', 'birth_date', 'last_name', 'is_active', 'is_admin',
        'is_content_manager')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class EditPatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('birth_date', 'gender', 'marital_Status','house_number','street','city',
        'state','zip_code','insurance_Provider','insurance_Policy_Number')


class DoctorCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Doctor
        fields = ('email', 'first_name', 'last_name', 'specialty')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            Doctor._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(DoctorCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class DoctorChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Doctor
        fields = ('email', 'password', 'first_name', 'last_name','specialty', 'is_active', 'is_admin',
        'is_content_manager')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class EditDoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('birth_date', 'gender', 'marital_Status','house_number','street','city',
        'state','zip_code','specialty','years_experience')

class NurseCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Nurse
        fields = ('email', 'first_name', 'last_name', 'department')

    def clean_email(self):
        email = self.cleaned_data["email"]

        try:
            Nurse._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(NurseCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class NurseChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Nurse
        fields = ('email', 'password', 'first_name', 'last_name','department', 'is_active', 'is_admin',
        'is_content_manager')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class EditNurseForm(ModelForm):
    class Meta:
        model = Nurse
        fields = ('birth_date', 'gender', 'marital_Status','house_number','street','city',
        'state','zip_code','years_experience')
        
class UserCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'birth_date')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            MyUser._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('duplicate email')
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'first_name', 'birth_date', 'last_name', 'is_active', 'is_admin',
        'is_content_manager')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
	

class PatAppointmentCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = Appointment
        fields = ('startTime', 'endTime', 'doctor', 'purpose')
        exclude = ('patient',)

class DocAppointmentCreationForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = Appointment
        fields = ('startTime', 'endTime', 'patient', 'purpose')
        exclude = ('doctor',)

class BillPayForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = Bill
        fields = ('status',)

class ReleaseBillForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = Bill
        fields = ('released',)

class ReleaseDocPayForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = Doctor
        fields = ('release_paycheck',)

class ReleaseNurPayForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = Nurse
        fields = ('release_paycheck',)

class BillApptForm(ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = Appointment
        fields = ('billed',)
    
class MedicalHistoryForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field."""

    class Meta:
        model = Patient
        fields = ('prescriptions', 'allergies')
