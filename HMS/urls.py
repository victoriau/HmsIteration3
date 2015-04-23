from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from HMS import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'login', views.login, name='login'),
    url(r'registration', views.registration, name='registration'),
    url(r'patient_home', views.patient_home, name='patient_home'),
    url(r'doctor_home', views.doctor_home, name='doctor_home'),
    url(r'nurse_home', views.nurse_home, name='nurse_home'),
    url(r'admin_home', views.admin_home, name='admin_home'),
    url(r'addNurse', views.add_Nurse, name='add_Nurse'),
    url(r'addDoctor', views.add_Doctor, name='add_Doctor'),
    url(r'addPatient', views.add_Patient, name='add_Patient'),
    url(r'patientCreateAppt/(?P<patient_id>[0-9]+)/$', views.create_Pat_Appt, name='create_pat_appt'),
    url(r'doctorCreateAppt/(?P<doctor_id>[0-9]+)/$', views.create_Doc_Appt, name='create_doc_appt'),
    url(r'^deleteAppt/(?P<id>\d+)/$', views.delete_Appt, name='delete_appt'),
    url(r'^changeAppt/(?P<id>\d+)/$', views.change_Appt, name='change_appt'),
    url(r'^payBill/(?P<id>\d+)/$', views.pay_Bill, name='pay_bill'),
    url(r'^releaseBill/(?P<id>\d+)/$', views.release_Bill, name='release_bill'),
    url(r'^endTreatment/(?P<id>\d+)/$', views.bill_Appt, name='bill_appt'),
    url(r'confirmation', views.bill_Paid, name='bill_paid'),
    url(r'^pdf/(?P<id>\d+)/$', views.pdf_gen, name = 'pdfgen'),
    url(r'^billDetail/(?P<id>\d+)/$', views.bill_Detail, name='bill_detail'),
    url(r'home', views.home, name = 'home'),
    url(r'medicalHistory', views.medical_history, name = 'medical_history'),
    url(r'^patients/(?P<patient_id>[0-9]+)/$', views.patient_detail, name='patdetail'),
    url(r'^doctors/(?P<doctor_id>[0-9]+)/$', views.doctor_detail, name='docdetail'),
    url(r'calendarHome', views.cal_home, name='cal_home'),
    url(r'^swingtime/events/type/([^/]+)/$', views.event_type, name='Hospital-event'),
    (r'^swingtime/', include('swingtime.urls')),
    url(r'^account/confirm/doctor/(?P<activation_key>\w+)/', ('HMS.views.register_confirm_doctor')),
    url(r'^account/confirm/nurse/(?P<activation_key>\w+)/', ('HMS.views.register_confirm_nurse')),
    url(r'^account/confirm/patient/(?P<activation_key>\w+)/', ('HMS.views.register_confirm_patient')),
    #(r'^accounts/', include('allauth.urls')),
    url(r'changePatient', views.change_Patient, name='change_Patient'),                     
    url(r'changePCP/(?P<patient_id>[0-9]+)/$', views.change_PCP, name='change_PCP'),                     
    #Password change
    url(r'^accounts/password_change/$', 
        'django.contrib.auth.views.password_change', 
        {'post_change_redirect' : 'HMS/passwordChanged'}, 
        name="password_change"),
    url(r'passwordChanged', views.passwordChanged, name = 'pChanged'),
   # url(r'^accounts/edit/$', 'django.contrib.auth.views.change_form', name = "edit"),
)

urlpatterns += staticfiles_urlpatterns()
