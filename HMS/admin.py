from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from HMS.models import MyUser, Nurse, Doctor, Patient, Appointment, Bill
from HMS.forms import (NurseCreationForm, NurseChangeForm, UserCreationForm, UserChangeForm,
                       DoctorCreationForm, DoctorChangeForm, PatientChangeForm, PatientCreationForm)

class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_content_manager')
    list_filter = ('is_admin', 'is_content_manager')
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date',
                                   'phone_number', 'gender', 'marital_Status')}),
        ('Address', {'fields': ('house_number', 'street', 'city', 'state', 'zip_code')}),
        ('Emergency Contact', {'fields': ('name', 'relation', 'primary_Phone', 'secondary_Phone')}),
        ('Permissions', {'fields': ('is_admin', 'is_content_manager')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class NurseAdmin(UserAdmin):
    # The forms to add and change user instances
    form = NurseChangeForm
    add_form = NurseCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'department', 'is_admin', 'is_content_manager')
    list_filter = ('is_admin', 'is_content_manager')
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date',
                                   'phone_number', 'gender', 'marital_Status', 'department')}),
        ('Address', {'fields': ('house_number', 'street', 'city', 'state', 'zip_code')}),
        ('Emergency Contact', {'fields': ('name', 'relation', 'primary_Phone', 'secondary_Phone')}),
        ('Nurse Pay', {'fields':('years_experience', 'salary', 'release_paycheck')}),
        ('Permissions', {'fields': ('is_admin', 'is_content_manager', 'is_active', 'department')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class AppointmentInline(admin.StackedInline):
    model = Appointment
    extra = 0

class BillInline(admin.StackedInline):
    model = Bill
    extra = 0
    
class DoctorAdmin(UserAdmin):
    # The forms to add and change user instances
    form = DoctorChangeForm
    add_form = DoctorCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_content_manager')
    list_filter = ('is_admin', 'is_content_manager')
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date',
                                   'phone_number', 'gender', 'marital_Status')}),
        ('Address', {'fields': ('house_number', 'street', 'city', 'state', 'zip_code')}),
        ('Emergency Contact', {'fields': ('name', 'relation', 'primary_Phone', 'secondary_Phone')}),
        ('Doctor Details', {'fields': ('degree', 'specialty', 'years_experience', 'salary', 'release_paycheck')}),
        ('Permissions', {'fields': ('is_admin', 'is_content_manager', 'is_active')}),
    )
    inlines = [AppointmentInline]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    
class PatientAdmin(UserAdmin):
    # The forms to add and change user instances
    form = PatientChangeForm
    add_form = PatientCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'is_admin', 'is_content_manager')
    list_filter = ('is_admin', 'is_content_manager')
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'password', 'first_name', 'last_name', 'birth_date',
                                   'phone_number', 'gender', 'marital_Status')}),
        ('Address', {'fields': ('house_number', 'street', 'city', 'state', 'zip_code')}),
        ('Emergency Contact', {'fields': ('name', 'relation', 'primary_Phone', 'secondary_Phone')}),
        ('Patient Details', {'fields': ('department','medical_History', 'insurance_Provider', 'insurance_Policy_Number')}),
		#('Medical History', {'fields': ('allergies', 'prescriptions')}),
        ('Permissions', {'fields': ('is_admin', 'is_content_manager','is_active', 'primaryCareProvider')}),
    )
    inlines = [AppointmentInline, BillInline]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient','doctor', 'purpose', 'startTime', 'billed', 'back')
    search_fields = ('purpose',)
    ordering = ('startTime',)
    inlines = [BillInline]

class BillAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'patient','amount', 'dueDate', 'released', 'back')
    search_fields = ('patient',)
    ordering = ('dueDate',)

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Bill, BillAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


