from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from HMS.forms import (NurseCreationForm, NurseChangeForm, UserCreationForm,
                       UserChangeForm, DoctorCreationForm, DoctorChangeForm,
                       PatientChangeForm, PatientCreationForm, MedicalHistoryForm,
                       PCPChangeForm, PatAppointmentCreationForm, ApptChangeForm,
                       DocAppointmentCreationForm, BillPayForm, ReleaseBillForm,
                       BillApptForm, ReleaseDocPayForm, ReleaseNurPayForm,
                       EditPatientForm, EditDoctorForm, EditNurseForm)
from django.core.urlresolvers import reverse
from HMS.models import MyUser, Nurse, Doctor, Patient, Appointment, Bill
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.mail import send_mail
import hashlib, random, datetime
from datetime import timedelta
from swingtime import models as swingtime
from django.utils import timezone
from django.views import generic
from django.shortcuts import render_to_response, get_object_or_404
from reportlab.pdfgen import canvas
from django.core.mail.message import EmailMessage
from django.conf import settings
from decimal import Decimal
import os

def login(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'HMS/home.html')

def passwordChanged(request):
    return render(request, 'HMS/passwordChangeComplete.html')
def registration(request):
    return render(request, 'HMS/Registration/registration.html')

def patient_home(request):
    doctor_list = Doctor.objects.order_by('-last_name')[:25]
    today = datetime.date.today()
    context = {'doctor_list': doctor_list, 'today': today}
    return render(request, 'HMS/PatientHome/patient_home.html', context)

def doctor_home(request):
    patient_list = Patient.objects.order_by('-last_name')[:25]
    today = datetime.date.today()
    context = {'patient_list': patient_list, 'today': today}
    return render(request, 'HMS/DoctorHome/doctor_home.html', context)

def cal_home(request):
    return render(request, 'HMS/swingtime/cal_home.html')

def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'HMS/Details/patient.html', {'patient': patient})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'HMS/Details/doctor.html', {'doctor': doctor})

def bill_Detail(request, id):
    bill = get_object_or_404(Bill, pk=id)
    return render(request, 'HMS/billDetail.html', {'bill': bill})
    
def nurse_home(request):
    patient_list = Patient.objects.order_by('-last_name')[:25]
    context = {'patient_list': patient_list}
    return render(request, 'HMS/NurseHome/nurse_home.html', context)

def admin_home(request):
    patient_list = Patient.objects.order_by('-last_name')[:25]
    bill_list = Bill.objects.order_by('-dueDate')[:25]
    doctor_list = Doctor.objects.order_by('-last_name')[:25]
    nurse_list = Nurse.objects.order_by('-last_name')[:25]
    appt_list = Appointment.objects.order_by('-startTime')[:25]
    context = {'patient_list': patient_list, 'bill_list':bill_list, 'doctor_list':doctor_list, 'nurse_list':nurse_list, 'appt_list':appt_list}
    return render(request, 'HMS/adminHome.html', context)

def event_type(request, abbr):
    event_type = get_object_or_404(swingtime.EventType, abbr=abbr)
    now = datetime.now()
    occurrences = swingtime.Occurrence.objects.filter(
        event__event_type=event_type,
        start_time__gte=now,
        start_time__lte=now+timedelta(days=+30)
    )
    return render_to_response(
        'HMS/upcoming_by_event_type.html', 
        dict(occurrences=occurrences, event_type=event_type),
        context_instance=RequestContext(request)
    )
    
#HMS/addNurse/
def add_Nurse(request):
    form_class = NurseCreationForm
    template_name = 'HMS/addNurse.html'

    #permitted = request.user.is_content_manager or request.user.is_admin

    #if not permitted:
        #raise PermissionDenied
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = form_class(request.POST)
        args['form'] = form
        form.instance.content_manager = request.user
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            user_profile = get_object_or_404(Nurse, email=email)
            user = user_profile
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user.activation_key=activation_key
            user.key_expires=key_expires
            user.is_active= False
            user.save()
            
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/HMS/account/confirm/nurse/%s" % (email, activation_key)

            send_mail(email_subject, email_body, 'hospmgmtad@gmail.com',
                [email], fail_silently=False)

            #return HttpResponseRedirect('/accounts/register_success')
            return HttpResponseRedirect('/verification_sent.html')
        else:
            args['form'] = NurseCreationForm()
            
            return HttpResponseRedirect('HMS/nurse_homepage')
        #else:
            return render(request, template_name, {'form': form})
    else:
        form = form_class()
        return render(request, template_name, {'form': form})
    
def edit_Nurse(request, id):
    nur = Nurse.objects.get(id=id)
    form  = EditNurseForm(request.POST or None, instance=nur)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect('HMS/home')
    return render(request, 'HMS/editProfile.html', {'form': form})

#HMS/addDoctor/
def add_Doctor(request):
    form_class = DoctorCreationForm
    template_name = 'HMS/addDoctor.html'

    #permitted = request.user.is_content_manager or request.user.is_admin

    #if not permitted:
        #raise PermissionDenied

    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = form_class(request.POST)
        args['form'] = form
        form.instance.content_manager = request.user
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            user_profile = get_object_or_404(Doctor, email=email)
            user = user_profile
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user.activation_key=activation_key
            user.key_expires=key_expires
            user.is_active= False
            user.save()
            
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/HMS/account/confirm/doctor/%s" % (email, activation_key)

            send_mail(email_subject, email_body, 'hospmgmtad@gmail.com',
                [email], fail_silently=False)

            #return HttpResponseRedirect('/accounts/register_success')
            return HttpResponseRedirect('/verification_sent.html')
        else:
            args['form'] = DoctorCreationForm()
            return HttpResponseRedirect('HMS/doctor_homepage')
       # else:
            return render(request, template_name, {'form': form})
    else:
        form = form_class()
        return render(request, template_name, {'form': form})

def edit_Doctor(request, id):
    doc = Doctor.objects.get(id=id)
    form  = EditDoctorForm(request.POST or None, instance=doc)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect('HMS/home')
    return render(request, 'HMS/editProfile.html', {'form': form})

#HMS/addPatient/
def add_Patient(request):
    form_class = PatientCreationForm
    template_name = 'HMS/addPatient.html'

    #permitted = request.user.is_content_manager or request.user.is_admin

    #if not permitted:
        #raise PermissionDenied

    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = form_class(request.POST)
        args['form'] = form
        form.instance.content_manager = request.user
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            user_profile = get_object_or_404(Patient, email=email)
            user = user_profile
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user.activation_key=activation_key
            user.key_expires=key_expires
            user.is_active= False
            user.save()
            

            email_subject = 'Account confirmation'
            #email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            #48hours http://127.0.0.1:8000/accounts/confirm/%s" % (email, activation_key)
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/HMS/account/confirm/patient/%s" % (email, activation_key)

            send_mail(email_subject, email_body, 'hospmgmtad@gmail.com',
                [email], fail_silently=False)

            #return HttpResponseRedirect('/accounts/register_success')
            return HttpResponseRedirect('HMS/verification_sent.html')
        else:
            args['form'] = PatientCreationForm()
            return HttpResponseRedirect('HMS/patient_homepage')
       # else:
            return render(request, template_name, {'form': form})
    else:
        form = form_class()
        return render(request, template_name, {'form': form})

def change_Patient(request):
    form_class = PatientChangeForm
    template_name = 'HMS/changePatient.html'

    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = form_class(request.POST)
        args['form'] = form
        form.instance.content_manager = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('HMS/Login/login.html')
        else:
            args['form'] = PatientChangeForm()
            return HttpResponseRedirect('HMS/patient_homepage')
            #return render(request, template_name, {'form': form})
    else:
        form = form_class()
        return render(request, template_name, {'form': form})

def edit_Patient(request, id):
    pat = Patient.objects.get(id=id)
    form  = EditPatientForm(request.POST or None, instance=pat)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect('HMS/home')
    return render(request, 'HMS/editProfile.html', {'form': form})    

def change_PCP(request, patient_id):
    instance = Patient.objects.get(id=patient_id)
    form  = PCPChangeForm(request.POST or None, instance=instance)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect('HMS/patient_homepage')
    return render(request, 'HMS/changePCP.html', {'form': form})

def create_Pat_Appt(request, patient_id):
    instance = Patient.objects.get(id=patient_id)
    if request.method == 'POST':
        form  = PatAppointmentCreationForm(request.POST or None)
        
        if form.is_valid():
            test = form.save(commit = False)
            test.patient = instance
            start = test.startTime
            patient = test.patient
            doctor = test.doctor
            test.save()
            email = patient.email
            email_subject = 'Appointment confirmation'
            email_body = "Hello, this email is to confirm that %s %s registered for an appointment at %s with Dr. %s. \
            We look forward to seeing you! If you have any questions or need to change your appointment email or call \
            us." % (patient.first_name, patient.last_name, start, doctor.last_name)

            mail= EmailMessage(email_subject, email_body, settings.EMAIL_HOST_USER, [email])
            #mail.attach(response,attach.read(), "application/pdf")
            mail.send()

            form = PatAppointmentCreationForm()
            return HttpResponseRedirect('HMS/patient_homepage')
    else:
        form = PatAppointmentCreationForm()
    return render(request, 'HMS/createAppt.html', {'form': form})

def create_Doc_Appt(request, doctor_id):
    instance = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form  = DocAppointmentCreationForm(request.POST or None)
        
        if form.is_valid():
            test = form.save(commit = False)
            test.doctor = instance
            test.save()

            form = DocAppointmentCreationForm()
            return HttpResponseRedirect('HMS/doctor_homepage')
    else:
        form = DocAppointmentCreationForm()
    return render(request, 'HMS/createAppt.html', {'form': form})

def delete_Appt(request, id):
    appt = get_object_or_404(Appointment, pk=id).delete()
    return HttpResponseRedirect('HMS/home')

def change_Appt(request, id):
    appointment = Appointment.objects.get(id=id)
    form  = ApptChangeForm(request.POST or None, instance=appointment)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect('HMS/home')
    return render(request, 'HMS/changeAppt.html', {'form': form, 'appointment':appointment})

def pay_Bill(request, id):
    instance = Bill.objects.get(id=id)
    form  = BillPayForm(request.POST or None, instance = instance, initial={'status': "Paid"})
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('HMS/confirmation')
    return render(request, 'HMS/billPay.html', {'form': form, 'bill':instance})

def bill_Paid(request):
    return render(request, 'HMS/billPaid.html')

def verification(request):
    return render(request, 'HMS/verification_sent.html')

def bill_Released(request):
    return render(request, 'HMS/billReleased.html')

def pay_Released(request):
    return render(request, 'HMS/payReleased.html')

def release_Doc_Pay(request, id):
    doctor = Doctor.objects.get(id=id)
    form = ReleaseDocPayForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        response = HttpResponse(content_type = 'application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Paystub.pdf"'
			
        p = canvas.Canvas(response)
        today = datetime.date.today()

        paystub_path = os.path.join(os.path.dirname(__file__), 'paystub.jpg')
        annual_salary = int(doctor.salary)
        monthly_salary = int(doctor.salary/Decimal(12))
        state_tax = int(monthly_salary*Decimal(0.05))
        federal_tax = int(monthly_salary*Decimal(0.06))
        monthly_pay = monthly_salary - state_tax - federal_tax
        ytd_pay = monthly_salary*today.month

        p.drawImage(paystub_path,5,400,width = 590, height = 350, preserveAspectRatio=False, anchor='c')
        p.drawString(20, 670, doctor.first_name + " " + doctor.last_name)
        p.drawString(220, 670, doctor.specialty)
        p.drawString(320, 670, str(doctor.years_experience) + " years")
        p.drawString(440, 670, str(today.month) + "-" + str(today.month) + "-" + str(today.year))
        p.drawString(440, 630, "$" + str(annual_salary))
        p.drawString(440, 610, "$" + str(monthly_salary))
        p.drawString(440, 585, "($" + str(state_tax) + ")")
        p.drawString(440, 570, "($" + str(federal_tax) + ")")
        p.drawString(440, 435, "$" + str(monthly_pay))
        p.drawString(440, 410, "$" + str(ytd_pay))
        p.showPage()
        p.save()
        
        email = doctor.email
        email_subject = 'Earnings Statement'
        email_body = "Hello, you have a new monthly earning statement. Please see the attached file"

        mail= EmailMessage(email_subject, email_body, settings.EMAIL_HOST_USER, [email])
        mail.attach("Paystub.pdf", response.content, "application/pdf")
        mail.send()
        return HttpResponseRedirect('/HMS/Released')
    return render(request, 'HMS/releasePay.html', {'form':form})

def release_Nur_Pay(request, id):
    nurse = Nurse.objects.get(id=id)
    form = ReleaseNurPayForm(request.POST or None, instance=nurse)
    if form.is_valid():
        form.save()
        response = HttpResponse(content_type = 'application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Paystub.pdf"'
			
        p = canvas.Canvas(response)
        today = datetime.date.today()

        paystub_path = os.path.join(os.path.dirname(__file__), 'paystub.jpg')
        annual_salary = int(nurse.salary)
        monthly_salary = int(nurse.salary/Decimal(12))
        state_tax = int(monthly_salary*Decimal(0.05))
        federal_tax = int(monthly_salary*Decimal(0.06))
        monthly_pay = monthly_salary - state_tax - federal_tax
        ytd_pay = monthly_salary*today.month

        p.drawImage(paystub_path,5,400,width = 590, height = 350, preserveAspectRatio=False, anchor='c')
        p.drawString(20, 670, nurse.first_name + " " + nurse.last_name)
        p.drawString(220, 670, nurse.department)
        p.drawString(320, 670, str(nurse.years_experience) + " years")
        p.drawString(440, 670, str(today.month) + "-" + str(today.month) + "-" + str(today.year))
        p.drawString(440, 630, "$" + str(annual_salary))
        p.drawString(440, 610, "$" + str(monthly_salary))
        p.drawString(440, 585, "($" + str(state_tax) + ")")
        p.drawString(440, 570, "($" + str(federal_tax) + ")")
        p.drawString(440, 435, "$" + str(monthly_pay))
        p.drawString(440, 410, "$" + str(ytd_pay))
        p.showPage()
        p.save()
        
        email = nurse.email
        email_subject = 'Earnings Statement'
        email_body = "Hello, you have a new monthly earning statement. Please see the attached file"

        mail= EmailMessage(email_subject, email_body, settings.EMAIL_HOST_USER, [email])
        mail.attach("Paystub.pdf", response.content, "application/pdf")
        mail.send()
        return HttpResponseRedirect('/HMS/Released')
    return render(request, 'HMS/releasePay.html', {'form':form})

def view_Nur_Pay(request, id):
    nurse = Nurse.objects.get(id=id)
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Paystub.pdf"'
			
    p = canvas.Canvas(response)
    today = datetime.date.today()
    paystub_path = os.path.join(os.path.dirname(__file__), 'paystub.jpg')
    annual_salary = int(nurse.salary)
    monthly_salary = int(nurse.salary/Decimal(12))
    state_tax = int(monthly_salary*Decimal(0.05))
    federal_tax = int(monthly_salary*Decimal(0.06))
    monthly_pay = monthly_salary - state_tax - federal_tax
    ytd_pay = monthly_salary*today.month

    p.drawImage(paystub_path,5,400,width = 590, height = 350, preserveAspectRatio=False, anchor='c')
    p.drawString(20, 670, nurse.first_name + " " + nurse.last_name)
    p.drawString(220, 670, nurse.department)
    p.drawString(320, 670, str(nurse.years_experience) + " years")
    p.drawString(440, 670, str(today.month) + "-" + str(today.month) + "-" + str(today.year))
    p.drawString(440, 630, "$" + str(annual_salary))
    p.drawString(440, 610, "$" + str(monthly_salary))
    p.drawString(440, 585, "($" + str(state_tax) + ")")
    p.drawString(440, 570, "($" + str(federal_tax) + ")")
    p.drawString(440, 435, "$" + str(monthly_pay))
    p.drawString(440, 410, "$" + str(ytd_pay))
    p.showPage()
    p.save()
        
    return response

def view_Doc_Pay(request, id):
    doctor = Doctor.objects.get(id=id)
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Paystub.pdf"'
			
    p = canvas.Canvas(response)
    today = datetime.date.today()

    paystub_path = os.path.join(os.path.dirname(__file__), 'paystub.jpg')
    annual_salary = int(doctor.salary)
    monthly_salary = int(doctor.salary/Decimal(12))
    state_tax = int(monthly_salary*Decimal(0.05))
    federal_tax = int(monthly_salary*Decimal(0.06))
    monthly_pay = monthly_salary - state_tax - federal_tax
    ytd_pay = monthly_salary*today.month

    p.drawImage(paystub_path,5,400,width = 590, height = 350, preserveAspectRatio=False, anchor='c')
    p.drawString(20, 670, doctor.first_name + " " + doctor.last_name)
    p.drawString(220, 670, doctor.specialty)
    p.drawString(320, 670, str(doctor.years_experience) + " years")
    p.drawString(440, 670, str(today.month) + "-" + str(today.month) + "-" + str(today.year))
    p.drawString(440, 630, "$" + str(annual_salary))
    p.drawString(440, 610, "$" + str(monthly_salary))
    p.drawString(440, 585, "($" + str(state_tax) + ")")
    p.drawString(440, 570, "($" + str(federal_tax) + ")")
    p.drawString(440, 435, "$" + str(monthly_pay))
    p.drawString(440, 410, "$" + str(ytd_pay))
    p.showPage()
    p.save()
        
    return response

def release_Bill(request, id):
    bill = Bill.objects.get(id=id)
    form  = ReleaseBillForm(request.POST or None, instance=bill)
    if form.is_valid():
            form.save()
            patient = bill.patient
            response = HttpResponse(content_type = 'application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Invoice.pdf"'

            p = canvas.Canvas(response)
            appts = Appointment.objects.all()
            invoice_path = os.path.join(os.path.dirname(__file__), 'invoice.jpg')
            contact_path = os.path.join(os.path.dirname(__file__), 'contact.jpg')
            p.drawImage(invoice_path, 0, 100, width=600, height=750, preserveAspectRatio=False, anchor='c')
            p.drawImage(contact_path, 0, 0, width=130, height=120, preserveAspectRatio=False, anchor='c')
            p.drawString(35,718, patient.first_name + " " + patient.last_name)
            p.drawString(35,703, str(patient.house_number) + " " + patient.street)
            p.drawString(35,688, patient.city + ", " + patient.state + " " + patient.zip_code)
            p.drawString(247,720, patient.primaryCareProvider.first_name + " " + patient.primaryCareProvider.last_name + ", " + patient.primaryCareProvider.degree)
            appts = Appointment.objects.all()
            num = 1
            i = bill.appointment      
            p.drawString(157,654 - num*22, i.startTime.strftime('%d-%m-%Y'))
            p.drawString(232,654 - num*22, i.purpose)
            p.drawString(400,654 - num*22, i.doctor.last_name)
            p.drawString(500,654 - num*22, "$" + str(bill.amount))
            p.drawString(500, 358 , "$" + str(bill.amount))
            p.showPage()
            p.save()
            email = patient.email
            email_subject = 'Billing Statement'
            email_body = "Hello, you have a new bill ready for payment. An invoice is attached to this email."

            mail= EmailMessage(email_subject, email_body, settings.EMAIL_HOST_USER, [email])
            mail.attach("Invoice.pdf", response.content, "application/pdf")
            mail.send()
            return HttpResponseRedirect('/HMS/Sent')
    return render(request, 'HMS/releaseBill.html', {'form': form})


def pdf_gen(request, id):
        bill = Bill.objects.get(id=id)
        patient = bill.patient
        response = HttpResponse(content_type = 'application/pdf')
        response['Content-Disposition'] = 'attachment; filename="PatientReport.pdf"'

        p = canvas.Canvas(response)
        appts = Appointment.objects.all()
        invoice_path = os.path.join(os.path.dirname(__file__), 'invoice.jpg')
        contact_path = os.path.join(os.path.dirname(__file__), 'contact.jpg')
        p.drawImage(invoice_path, 0, 100, width=600, height=750, preserveAspectRatio=False, anchor='c')
        p.drawImage(contact_path, 0, 0, width=130, height=120, preserveAspectRatio=False, anchor='c')
        p.drawString(35,718, patient.first_name + " " + patient.last_name)
        p.drawString(35,703, str(patient.house_number) + " " + patient.street)
        p.drawString(35,688, patient.city + ", " + patient.state + " " + patient.zip_code)
        p.drawString(247,720, patient.primaryCareProvider.first_name + " " + patient.primaryCareProvider.last_name + ", " + patient.primaryCareProvider.degree)
        appts = Appointment.objects.all()
        num = 1
        i = bill.appointment      
        p.drawString(157,654 - num*22, i.startTime.strftime('%d-%m-%Y'))
        p.drawString(232,654 - num*22, i.purpose)
        p.drawString(400,654 - num*22, i.doctor.last_name)
        p.drawString(500,654 - num*22, "$" + str(bill.amount))
        p.drawString(500, 358 , "$" + str(bill.amount))
        p.showPage()
        p.save()
        return response
    
def bill_Appt(request, id):
    instance = Appointment.objects.get(id=id)
    form  = BillApptForm(request.POST or None, instance=instance)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect('HMS/home')
    return render(request, 'HMS/billAppt.html', {'form': form})
"""def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.MyUser.is_authenticated():
        HttpResponseRedirect('HMS/doctor_homepage')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(MyUser, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
#    if user_profile.key_expires < timezone.now():
     #   return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.MyUser
    MyUser.is_active = True
    MyUser.save()
    return render_to_response('user_profile/confirm.html')"""

def register_confirm(request, activation_key):
    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(Doctor, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('account/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return render(request, 'HMS/account/confirm.html')

"""def register_confirm_doctor(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.Doctor.is_authenticated():
        HttpResponseRedirect('HMS/doctor_homepage')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(Doctor, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
#    if user_profile.key_expires < timezone.now():
     #   return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.Doctor
    Doctor.is_active = True
    Doctor.save()
    return render_to_response('user_profile/confirm.html')"""
	
def register_confirm_doctor(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    user_profile = get_object_or_404(Doctor, activation_key=activation_key)
    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('account/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return render(request, 'HMS/account/confirm.html')

"""def register_confirm_nurse(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.Nurse.is_authenticated():
        HttpResponseRedirect('HMS/nurse_homepage')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(Nurse, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
#    if user_profile.key_expires < timezone.now():
     #   return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.Nurse
    Nurse.is_active = True
    Nurse.save()
    return render_to_response('user_profile/confirm.html')"""

def register_confirm_nurse(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    user_profile = get_object_or_404(Nurse, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('account/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return render(request, 'HMS/account/confirm.html')
	
"""def register_confirm_patient(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.Patient.is_authenticated():
        HttpResponseRedirect('HMS/doctor_homepage')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(Patient, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    #check if the activation key has expired, if it hase then render confirm_expired.html
#    if user_profile.key_expires < timezone.now():
     #   return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.Patient
    Patient.is_active = True
    Patient.save()
    return render(request, 'user_profile/confirm.html')"""

def register_confirm_patient(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    user_profile = get_object_or_404(Patient, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('account/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile
    user.is_active = True
    user.save()
    return render(request, 'HMS/account/confirm.html')


def medical_history(request):
    form_class = MedicalHistoryForm
    template_name = 'HMS/medicalHistory.html'

    #permitted = request.user.is_content_manager or request.user.is_admin

    #if not permitted:
        #raise PermissionDenied
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = form_class(request.POST)
        args['form'] = form
        form.instance.content_manager = request.user
        if form.is_valid():
            form.save()
            #user.save()

            #return HttpResponseRedirect('/accounts/register_success')
            return HttpResponseRedirect('../home.html')
        else:
            args['form'] = MedicalHistoryForm()
            
            return HttpResponseRedirect('HMS/medicalRecord.html')
        #else:
            return render(request, template_name, {'form': form})
    else:
        form = form_class()
        return render(request, template_name, {'form': form})

