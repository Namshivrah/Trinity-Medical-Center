from django.shortcuts import render,redirect,reverse
from .models import Patient, GENDERS, AppointmentRequest, Doctor, MedicalRecord, TYPE, Test_result, MedicalImage, TreatmentPlan, Bill, METHOD, ExtendedUser
from .forms import *
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login


# Create your views here.

# --------------------NAVBAR VIEWS--------------------
def home_view(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')

def aboutus_view(request):
    return render(request,'hospital/aboutus.html')

def contactus_view(request):
    return render(request, 'hospital/contact_us.html')

# -----------------------LOGIN VIEWS---------------------

def patientdept_signupview(request):
    if request.method == 'POST':
        form = MyAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect the user to a protected page or another page
                return redirect('protected_page')
            else:
                # Handle invalid login credentials
                pass  # You may display an error message to the user
    else:
        form = MyAuthenticationForm()
    return render(request, 'hospital/patientdeptsignup.html', {'form': form})

def recordsdept_signupview(request):
    if request.method == 'POST':
        form = MyAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect the user to a protected page or another page
                return redirect('protected_page')
            else:
                # Handle invalid login credentials
                pass  # You may display an error message to the user
    else:
        form = MyAuthenticationForm()
    return render(request, 'hospital/recordsdeptsignup.html', {'form': form})

def financedept_signupview(request):
    if request.method == 'POST':
        form = MyAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect the user to a protected page or another page
                return redirect('protected_page')
            else:
                # Handle invalid login credentials
                pass  # You may display an error message to the user
    else:
        form = MyAuthenticationForm()
    return render(request, 'hospital/financedeptsignup.html', {'form': form})


def patient_dept_create(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']   
        if password1 == password2:
            user = ExtendedUser.objects.create_user(
                username=request.POST['username'],
                password=password1,
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST.get('email'),
                department = request.POST['department'],

            )
            group, created = Group.objects.get_or_create(name='Patient Management')
            user.groups.add(group)
            return redirect('patient_dept_signup')
        else:
            print('Passwords do not match')

    return render(request, 'hospital/patient_dept_signup.html', { 'DEPARTMENT_CHOICES': ExtendedUser.DEPARTMENT_CHOICES,})

def records_dept_create(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']   
        if password1 == password2:
            user = ExtendedUser.objects.create_user(
                username=request.POST['username'],
                password=password1,
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST.get('email'),
                department = request.POST['department'],

            )
            group, created = Group.objects.get_or_create(name='Records Management')
            user.groups.add(group)
            return redirect('records_dept_signup')
        else:
            print('Passwords do not match')

    return render(request, 'hospital/record_dept_create.html', { 'DEPARTMENT_CHOICES': ExtendedUser.DEPARTMENT_CHOICES, })

def financial_dept_create(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']   
        if password1 == password2:
            user = ExtendedUser.objects.create_user(
                username=request.POST['username'],
                password=password1,
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST.get('email'),
                department = request.POST['department'],
            )
            group, created = Group.objects.get_or_create(name='Financial Management')
            user.groups.add(group)
            return redirect('finance_dept_signup')
        else:
            print('Passwords do not match')

    return render(request, 'hospital/finance_dept_create.html', { 'DEPARTMENT_CHOICES': ExtendedUser.DEPARTMENT_CHOICES,})



# --------------Dashboards----------
def home_dashboard1(request):
    return render(request, 'hospital/home_dashboard1.html')

def home_dashboard2(request):
    return render(request, 'hospital/home_dashboard2.html')

def home_dashboard3(request):
    return render(request, 'hospital/home_dashboard3.html')

# ---------------Patient Management Department

def patient_register(request):
    submitted = False
    if request.method =='POST':
        print(1)
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            gender = request.POST['gender']
            date_of_birth = request.POST['date_of_birth']
            telephone = request.POST['telephone']
            email = request.POST['email']
            ward_village = request.POST['ward_village']
            city = request.POST['city']
            country = request.POST['country']
            
            print(42)
            
            # Create an instance of the Voters model
            new_patient = Patient(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                date_of_birth=date_of_birth,
                telephone=telephone,
                email=email,
                ward_village=ward_village,
                city=city,
                country=country,
            )
            print(6)
            if Patient.objects.filter(telephone=telephone).exists():
                #messages.error(request, 'Error: Phone contact already exists. Please check and try again.')
                return HttpResponse("Error: Phone contact already exists. Please check and try again.")
                
            
            else:
                new_patient.save()
                #messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse('register_patient') + '?submitted=True')
                #return HttpResponse("Thank you for registering")

        else:
            print(form.errors)
    else:
        # If the request method is not POST, create a new form
        print(8)
        form = PatientRegistrationForm()
        if 'submitted' in request.GET:
             submitted = True
        print(9)
    return render(request, 'hospital/registerpatient.html',{'form':form, 'submitted':submitted, 'GENDERS': GENDERS})



def request_appointment(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    submitted = False
    if request.method =='POST':
        print(1)
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            print(2)
            patient_id = request.POST.get('patient')
            doctor_id = request.POST.get('doctor')
            preferred_date = request.POST['preferred_date']
            preferred_time = request.POST['preferred_time']
            reason_to_visit = request.POST['reason_to_visit']
            additional_notes = request.POST['additional_notes']
        
            # Create an instance of the Voters model
            new_appointment_request = AppointmentRequest(
                patient_id =patient_id ,
                doctor_id =doctor_id ,
                preferred_date=preferred_date,
                preferred_time=preferred_time,
                reason_to_visit=reason_to_visit,
                additional_notes=additional_notes,

            )

            existing_appointment_request = AppointmentRequest.objects.filter(
                patient_id=patient_id,
                doctor_id=doctor_id,
                preferred_date=preferred_date,
                preferred_time=preferred_time
            ).first()

            print(6)
            if existing_appointment_request:
                #messages.error(request, 'Error: NIN number already exists. Please check and try again.')
                return HttpResponse("Error: Appointment exists. Please check and try again.")
                #context = {'nin_error': True}
                return render(request, 'registration/voter.html',{'form':form}) #context before form
                print(7)
            
            else:
                new_appointment_request.save()
                #messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse('request_appointment') + '?submitted=True')
                #return HttpResponse("Thank you for registering")

        else:
            print(form.errors)
    else:
        # If the request method is not POST, create a new form
        print(8)
        form = AppointmentRequestForm()
        if 'submitted' in request.GET:
             submitted = True
        print(9)

    return render(request, 'hospital/requestappointment.html',{'form':form, 'submitted':submitted, 'patients':patients, 'doctors':doctors})



def confirmed_appointments(request):
    appointments = AppointmentRequest.objects.all()
    return render(request, 'hospital/viewappointments.html', {'appointments':appointments})



# -----------------Recoeds Management Department..............

def edit_records(request):
    images = [
        'images/medic-rec.jpg'
        'images/test_results.jpg'
        'images/medical-imaging.jpg'
        'images/treat_plan.png'
    ]

    return render(request, 'hospital/edithealthrecords.html',{'images':images})



def medical_records(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    submitted = False
    if request.method =='POST':
        print(1)
        form = MedicalRecordsForm(request.POST)
        if form.is_valid():
            print(2)
            patient = request.POST.get('patient')
            doctor = request.POST.get('doctor')
            medical_history = request.POST['medical_history']
            notes = request.POST['notes']
            symptoms = request.POST['symptoms']
            diagnosis = request.POST['diagnosis']
            prescription = request.POST['prescription']
            current_medication = request.POST['current_medication']
            test_results = request.POST['test_results']
            date = request.POST['date']
            updated_by = request.POST['updated_by']
            updated = request.POST['updated']

            # Create an instance of the Voters model
            new_medical_record = MedicalRecord(
                patient =patient ,
                doctor =doctor ,
                medical_historypreferred_date=medical_history,
                notes=notes,
                symptoms=symptoms,
                diagnosis=diagnosis,
                prescription=prescription,
                current_medication=current_medication,
                test_results=test_results,
                date=date,
                updated_by=updated_by,
                updated=updated,
            )

            print(6)
            if Patient.objects.filter(id=id).exists():
                #messages.error(request, 'Error: NIN number already exists. Please check and try again.')
                return HttpResponse("Error: Medical record already exists. Please check and try again.")
                #context = {'nin_error': True}
                return render(request, 'registration/voter.html',{'form':form}) #context before form
                print(7)
            
            else:
                new_medical_record.save()
                #messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse('medical_records') + '?submitted=True')
                #return HttpResponse("Thank you for registering")

        else:
            print(form.errors)
    else:
        # If the request method is not POST, create a new form
        print(8)
        form = AppointmentRequestForm()
        if 'submitted' in request.GET:
             submitted = True
        print(9)

    return render(request, 'hospital/medical_records.html',{'form':form, 'submitted':submitted, 'patients':patients, 'doctors':doctors})



def test_results(request):
    medical_records = MedicalRecord.objects.all()
    submitted = False
    if request.method =='POST':
        print(1)
        form = TestResultForm(request.POST)
        if form.is_valid():
            health_record_id= request.POST.get('health_record')           
            health_record = MedicalRecord.object.get(id=health_record_id)
            test_type = request.POST['test_type']
            test_date = request.POST['test_date']
            test_result = request.POST['test_result']
            description = request.POST['description']
            updated_by = request.POST['updated_by']
            updated = request.POST['updated']            
            print(42)
            
            # Create an instance of the Voters model
            new_test_results = Test_result(
                health_record=health_record,
                test_type=test_type,
                test_date=test_date,
                test_result=test_result,
                description=description,
                updated_by=updated_by,
                updated=updated,
            )
            print(6)
            if MedicalRecord.objects.filter(id=id).exists():
                #messages.error(request, 'Error: Phone contact already exists. Please check and try again.')
                return HttpResponse("Error: Phone contact already exists. Please check and try again.")
                #context = {'phone_error': True}
                return render(request, 'registration/voter.html',{'form':form}) #context before form
                print(11)
            
            else:
                new_test_results.save()
                #messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse('test_results') + '?submitted=True')
                #return HttpResponse("Thank you for registering")

        else:
            print(form.errors)
    else:
        # If the request method is not POST, create a new form
        print(8)
        form = TestResultForm()
        if 'submitted' in request.GET:
             submitted = True
        print(9)
    return render(request, 'hospital/test_results.html',{'form':form, 'submitted':submitted, 'TYPE': TYPE,'medical_records':medical_records})



def medical_image(request):
    medical_records = MedicalRecord.objects.all()
    submitted = False
    if request.method =='POST':
        print(1)
        form = MedicalImageForm(request.POST)
        if form.is_valid():
            health_record_id= request.POST.get('health_record')           
            health_record = MedicalRecord.object.get(id=health_record_id)
            description = request.POST['description']
            updated_by = request.POST['updated_by']
            updated_on = request.POST['updated_on']            
            print(42)
            
            # Create an instance of the Voters model
            new_image = MedicalImage(
                health_record=health_record,
                description=description,
                updated_by=updated_by,
                updated_on=updated_on,
            )
            print(6)
            if MedicalRecord.objects.filter(id=id).exists():
                #messages.error(request, 'Error: Phone contact already exists. Please check and try again.')
                return HttpResponse("Error: Phone contact already exists. Please check and try again.")
                #context = {'phone_error': True}
                return render(request, 'registration/voter.html',{'form':form}) #context before form
                print(11)
            
            else:
                new_image.save()
                #messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse('medical_image') + '?submitted=True')
                #return HttpResponse("Thank you for registering")

        else:
            print(form.errors)
    else:
        # If the request method is not POST, create a new form
        print(8)
        form = MedicalImageForm()
        if 'submitted' in request.GET:
             submitted = True
        print(9)
    return render(request, 'hospital/medical_image.html',{'form':form, 'submitted':submitted, 'medical_records':medical_records})



def treatment_plan(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    medical_records = MedicalRecord.objects.all()
    submitted = False
    if request.method =='POST':
        print(1)
        form = TreatmentPlanForm(request.POST)
        if form.is_valid():
            print(2)
            patient_id = request.POST.get('patient')
            doctor_id = request.POST.get('doctor')
            health_record_id= request.POST.get('health_record')           
            health_record = MedicalRecord.object.get(id=health_record_id)
            treatment = request.POST['treatment']
            updated_by = request.POST['updated_by']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
        
            # Create an instance of the Voters model
            new_treatment_plan = TreatmentPlan(
                patient_id =patient_id ,
                doctor_id =doctor_id ,
                health_record=health_record,
                treatment=treatment,
                updated_by=updated_by,
                start_datereason_to_visit=start_date,
                end_date=end_date,

            )

           
            print(6)
            if MedicalRecord.objects.filter(id=id).exists():
                #messages.error(request, 'Error: Phone contact already exists. Please check and try again.')
                return HttpResponse("Error: Phone contact already exists. Please check and try again.")
                #context = {'phone_error': True}
                return render(request, 'registration/voter.html',{'form':form}) #context before form
                print(11)
            
            
            else:
                new_treatment_plan.save()
                #messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse('treatment_plan') + '?submitted=True')
                #return HttpResponse("Thank you for registering")

        else:
            print(form.errors)
    else:
        # If the request method is not POST, create a new form
        print(8)
        form = TreatmentPlanForm()
        if 'submitted' in request.GET:
             submitted = True
        print(9)

    return render(request, 'hospital/treatment_plan.html',{'form':form, 'submitted':submitted, 'patients':patients, 'doctors':doctors, 'medical_records':medical_records})


 
def view_record(request):
    query = request.GET.get('query')
    patients = Patient.objects.filter(first_name__icontains=query)
    medical_records = MedicalRecord.objects.filter(patient__in=patients)
    treatment_plans = TreatmentPlan.objects.filter(patient__in=patients)

    return render(request, 'view_record.html',{
        'query':query,
        'patients':patients,
        'medical_recrds':medical_records,
        'treatmet_plans':treatment_plans
    })



# ---------------FINANCIAL DEPARTMENT---------------------

def billing(request):

    patients = Patient.objects.all()
    submitted = False
    if request.method =='POST':
        print(1)
        form = BillForm(request.POST)
        if form.is_valid():
            patient_id= request.POST.get('patient')           
            bill_number = request.POST['bill_number']
            payment_method = request.POST['payment_method']
            total_amount = request.POST['total_amount']
            date = request.POST['date']
                      
            print(42)
            
            # Create an instance of the Voters model
            new_bills = Bill(
                patient_id=patient_id,
                bill_number=bill_number,
                payment_method=payment_method,
                total_amount =total_amount ,
                date=date,
                
            )
            print(6)
            if MedicalRecord.objects.filter(id=id).exists():
                #messages.error(request, 'Error: Phone contact already exists. Please check and try again.')
                return HttpResponse("Error: Phone contact already exists. Please check and try again.")
                #context = {'phone_error': True}
                return render(request, 'registration/voter.html',{'form':form}) #context before form
                print(11)
            
            else:
                new_bills.save()
                #messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse('billing') + '?submitted=True')
                #return HttpResponse("Thank you for registering")

        else:
            print(form.errors)
    else:
        # If the request method is not POST, create a new form
        print(8)
        form = BillForm()
        if 'submitted' in request.GET:
             submitted = True
        print(9)
    return render(request, 'hospital/billing.html',{'form':form, 'submitted':submitted, 'METHOD': METHOD,'patients':patients})
    









# def adminclick_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return render(request,'hospital/adminclick.html')


# #for showing signup/login button for doctor(by sumit)
# def doctorclick_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return render(request,'hospital/doctorclick.html')


# #for showing signup/login button for patient(by sumit)
# def patientclick_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return render(request,'hospital/patientclick.html')




# def admin_signup_view(request):
#     form=forms.AdminSigupForm()
#     if request.method=='POST':
#         form=forms.AdminSigupForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.set_password(user.password)
#             user.save()
#             my_admin_group = Group.objects.get_or_create(name='ADMIN')
#             my_admin_group[0].user_set.add(user)
#             return HttpResponseRedirect('adminlogin')
#     return render(request,'hospital/adminsignup.html',{'form':form})




# def doctor_signup_view(request):
#     userForm=forms.DoctorUserForm()
#     doctorForm=forms.DoctorForm()
#     mydict={'userForm':userForm,'doctorForm':doctorForm}
#     if request.method=='POST':
#         userForm=forms.DoctorUserForm(request.POST)
#         doctorForm=forms.DoctorForm(request.POST,request.FILES)
#         if userForm.is_valid() and doctorForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             doctor=doctorForm.save(commit=False)
#             doctor.user=user
#             doctor=doctor.save()
#             my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
#             my_doctor_group[0].user_set.add(user)
#         return HttpResponseRedirect('doctorlogin')
#     return render(request,'hospital/doctorsignup.html',context=mydict)


# def patient_signup_view(request):
#     userForm=forms.PatientUserForm()
#     patientForm=forms.PatientForm()
#     mydict={'userForm':userForm,'patientForm':patientForm}
#     if request.method=='POST':
#         userForm=forms.PatientUserForm(request.POST)
#         patientForm=forms.PatientForm(request.POST,request.FILES)
#         if userForm.is_valid() and patientForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             patient=patientForm.save(commit=False)
#             patient.user=user
#             patient.assignedDoctorId=request.POST.get('assignedDoctorId')
#             patient=patient.save()
#             my_patient_group = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group[0].user_set.add(user)
#         return HttpResponseRedirect('patientlogin')
#     return render(request,'hospital/patientsignup.html',context=mydict)






# #-----------for checking user is doctor , patient or admin(by sumit)
# def is_admin(user):
#     return user.groups.filter(name='ADMIN').exists()
# def is_doctor(user):
#     return user.groups.filter(name='DOCTOR').exists()
# def is_patient(user):
#     return user.groups.filter(name='PATIENT').exists()


# #---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
# def afterlogin_view(request):
#     if is_admin(request.user):
#         return redirect('admin-dashboard')
#     elif is_doctor(request.user):
#         accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
#         if accountapproval:
#             return redirect('doctor-dashboard')
#         else:
#             return render(request,'hospital/doctor_wait_for_approval.html')
#     elif is_patient(request.user):
#         accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
#         if accountapproval:
#             return redirect('patient-dashboard')
#         else:
#             return render(request,'hospital/patient_wait_for_approval.html')








# #---------------------------------------------------------------------------------
# #------------------------ ADMIN RELATED VIEWS START ------------------------------
# #---------------------------------------------------------------------------------
# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_dashboard_view(request):
#     #for both table in admin dashboard
#     doctors=models.Doctor.objects.all().order_by('-id')
#     patients=models.Patient.objects.all().order_by('-id')
#     #for three cards
#     doctorcount=models.Doctor.objects.all().filter(status=True).count()
#     pendingdoctorcount=models.Doctor.objects.all().filter(status=False).count()

#     patientcount=models.Patient.objects.all().filter(status=True).count()
#     pendingpatientcount=models.Patient.objects.all().filter(status=False).count()

#     appointmentcount=models.Appointment.objects.all().filter(status=True).count()
#     pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
#     mydict={
#     'doctors':doctors,
#     'patients':patients,
#     'doctorcount':doctorcount,
#     'pendingdoctorcount':pendingdoctorcount,
#     'patientcount':patientcount,
#     'pendingpatientcount':pendingpatientcount,
#     'appointmentcount':appointmentcount,
#     'pendingappointmentcount':pendingappointmentcount,
#     }
#     return render(request,'hospital/admin_dashboard.html',context=mydict)


# # this view for sidebar click on admin page
# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_doctor_view(request):
#     return render(request,'hospital/admin_doctor.html')



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_view_doctor_view(request):
#     doctors=models.Doctor.objects.all().filter(status=True)
#     return render(request,'hospital/admin_view_doctor.html',{'doctors':doctors})



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def delete_doctor_from_hospital_view(request,pk):
#     doctor=models.Doctor.objects.get(id=pk)
#     user=models.User.objects.get(id=doctor.user_id)
#     user.delete()
#     doctor.delete()
#     return redirect('admin-view-doctor')



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def update_doctor_view(request,pk):
#     doctor=models.Doctor.objects.get(id=pk)
#     user=models.User.objects.get(id=doctor.user_id)

#     userForm=forms.DoctorUserForm(instance=user)
#     doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
#     mydict={'userForm':userForm,'doctorForm':doctorForm}
#     if request.method=='POST':
#         userForm=forms.DoctorUserForm(request.POST,instance=user)
#         doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
#         if userForm.is_valid() and doctorForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             doctor=doctorForm.save(commit=False)
#             doctor.status=True
#             doctor.save()
#             return redirect('admin-view-doctor')
#     return render(request,'hospital/admin_update_doctor.html',context=mydict)




# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_doctor_view(request):
#     userForm=forms.DoctorUserForm()
#     doctorForm=forms.DoctorForm()
#     mydict={'userForm':userForm,'doctorForm':doctorForm}
#     if request.method=='POST':
#         userForm=forms.DoctorUserForm(request.POST)
#         doctorForm=forms.DoctorForm(request.POST, request.FILES)
#         if userForm.is_valid() and doctorForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()

#             doctor=doctorForm.save(commit=False)
#             doctor.user=user
#             doctor.status=True
#             doctor.save()

#             my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
#             my_doctor_group[0].user_set.add(user)

#         return HttpResponseRedirect('admin-view-doctor')
#     return render(request,'hospital/admin_add_doctor.html',context=mydict)




# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_approve_doctor_view(request):
#     #those whose approval are needed
#     doctors=models.Doctor.objects.all().filter(status=False)
#     return render(request,'hospital/admin_approve_doctor.html',{'doctors':doctors})


# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def approve_doctor_view(request,pk):
#     doctor=models.Doctor.objects.get(id=pk)
#     doctor.status=True
#     doctor.save()
#     return redirect(reverse('admin-approve-doctor'))


# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def reject_doctor_view(request,pk):
#     doctor=models.Doctor.objects.get(id=pk)
#     user=models.User.objects.get(id=doctor.user_id)
#     user.delete()
#     doctor.delete()
#     return redirect('admin-approve-doctor')



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_view_doctor_specialisation_view(request):
#     doctors=models.Doctor.objects.all().filter(status=True)
#     return render(request,'hospital/admin_view_doctor_specialisation.html',{'doctors':doctors})



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_patient_view(request):
#     return render(request,'hospital/admin_patient.html')



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_view_patient_view(request):
#     patients=models.Patient.objects.all().filter(status=True)
#     return render(request,'hospital/admin_view_patient.html',{'patients':patients})



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def delete_patient_from_hospital_view(request,pk):
#     patient=models.Patient.objects.get(id=pk)
#     user=models.User.objects.get(id=patient.user_id)
#     user.delete()
#     patient.delete()
#     return redirect('admin-view-patient')



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def update_patient_view(request,pk):
#     patient=models.Patient.objects.get(id=pk)
#     user=models.User.objects.get(id=patient.user_id)

#     userForm=forms.PatientUserForm(instance=user)
#     patientForm=forms.PatientForm(request.FILES,instance=patient)
#     mydict={'userForm':userForm,'patientForm':patientForm}
#     if request.method=='POST':
#         userForm=forms.PatientUserForm(request.POST,instance=user)
#         patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
#         if userForm.is_valid() and patientForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             patient=patientForm.save(commit=False)
#             patient.status=True
#             patient.assignedDoctorId=request.POST.get('assignedDoctorId')
#             patient.save()
#             return redirect('admin-view-patient')
#     return render(request,'hospital/admin_update_patient.html',context=mydict)





# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_patient_view(request):
#     userForm=forms.PatientUserForm()
#     patientForm=forms.PatientForm()
#     mydict={'userForm':userForm,'patientForm':patientForm}
#     if request.method=='POST':
#         userForm=forms.PatientUserForm(request.POST)
#         patientForm=forms.PatientForm(request.POST,request.FILES)
#         if userForm.is_valid() and patientForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()

#             patient=patientForm.save(commit=False)
#             patient.user=user
#             patient.status=True
#             patient.assignedDoctorId=request.POST.get('assignedDoctorId')
#             patient.save()

#             my_patient_group = Group.objects.get_or_create(name='PATIENT')
#             my_patient_group[0].user_set.add(user)

#         return HttpResponseRedirect('admin-view-patient')
#     return render(request,'hospital/admin_add_patient.html',context=mydict)



# #------------------FOR APPROVING PATIENT BY ADMIN----------------------
# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_approve_patient_view(request):
#     #those whose approval are needed
#     patients=models.Patient.objects.all().filter(status=False)
#     return render(request,'hospital/admin_approve_patient.html',{'patients':patients})



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def approve_patient_view(request,pk):
#     patient=models.Patient.objects.get(id=pk)
#     patient.status=True
#     patient.save()
#     return redirect(reverse('admin-approve-patient'))



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def reject_patient_view(request,pk):
#     patient=models.Patient.objects.get(id=pk)
#     user=models.User.objects.get(id=patient.user_id)
#     user.delete()
#     patient.delete()
#     return redirect('admin-approve-patient')



# #--------------------- FOR DISCHARGING PATIENT BY ADMIN START-------------------------
# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_discharge_patient_view(request):
#     patients=models.Patient.objects.all().filter(status=True)
#     return render(request,'hospital/admin_discharge_patient.html',{'patients':patients})



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def discharge_patient_view(request,pk):
#     patient=models.Patient.objects.get(id=pk)
#     days=(date.today()-patient.admitDate) #2 days, 0:00:00
#     assignedDoctor=models.User.objects.all().filter(id=patient.assignedDoctorId)
#     d=days.days # only how many day that is 2
#     patientDict={
#         'patientId':pk,
#         'name':patient.get_name,
#         'mobile':patient.mobile,
#         'address':patient.address,
#         'symptoms':patient.symptoms,
#         'admitDate':patient.admitDate,
#         'todayDate':date.today(),
#         'day':d,
#         'assignedDoctorName':assignedDoctor[0].first_name,
#     }
#     if request.method == 'POST':
#         feeDict ={
#             'roomCharge':int(request.POST['roomCharge'])*int(d),
#             'doctorFee':request.POST['doctorFee'],
#             'medicineCost' : request.POST['medicineCost'],
#             'OtherCharge' : request.POST['OtherCharge'],
#             'total':(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
#         }
#         patientDict.update(feeDict)
#         #for updating to database patientDischargeDetails (pDD)
#         pDD=models.PatientDischargeDetails()
#         pDD.patientId=pk
#         pDD.patientName=patient.get_name
#         pDD.assignedDoctorName=assignedDoctor[0].first_name
#         pDD.address=patient.address
#         pDD.mobile=patient.mobile
#         pDD.symptoms=patient.symptoms
#         pDD.admitDate=patient.admitDate
#         pDD.releaseDate=date.today()
#         pDD.daySpent=int(d)
#         pDD.medicineCost=int(request.POST['medicineCost'])
#         pDD.roomCharge=int(request.POST['roomCharge'])*int(d)
#         pDD.doctorFee=int(request.POST['doctorFee'])
#         pDD.OtherCharge=int(request.POST['OtherCharge'])
#         pDD.total=(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
#         pDD.save()
#         return render(request,'hospital/patient_final_bill.html',context=patientDict)
#     return render(request,'hospital/patient_generate_bill.html',context=patientDict)



# #--------------for discharge patient bill (pdf) download and printing
# import io
# from xhtml2pdf import pisa
# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse


# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = io.BytesIO()
#     pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return



# def download_pdf_view(request,pk):
#     dischargeDetails=models.PatientDischargeDetails.objects.all().filter(patientId=pk).order_by('-id')[:1]
#     dict={
#         'patientName':dischargeDetails[0].patientName,
#         'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
#         'address':dischargeDetails[0].address,
#         'mobile':dischargeDetails[0].mobile,
#         'symptoms':dischargeDetails[0].symptoms,
#         'admitDate':dischargeDetails[0].admitDate,
#         'releaseDate':dischargeDetails[0].releaseDate,
#         'daySpent':dischargeDetails[0].daySpent,
#         'medicineCost':dischargeDetails[0].medicineCost,
#         'roomCharge':dischargeDetails[0].roomCharge,
#         'doctorFee':dischargeDetails[0].doctorFee,
#         'OtherCharge':dischargeDetails[0].OtherCharge,
#         'total':dischargeDetails[0].total,
#     }
#     return render_to_pdf('hospital/download_bill.html',dict)



# #-----------------APPOINTMENT START--------------------------------------------------------------------
# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_appointment_view(request):
#     return render(request,'hospital/admin_appointment.html')

# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_rooms(request):
#     return render(request,'hospital/rooms.html')


# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_message(request):
#     return render(request,'hospital/admin-message.html')



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_view_appointment_view(request):
#     appointments=models.Appointment.objects.all().filter(status=True)
#     return render(request,'hospital/admin_view_appointment.html',{'appointments':appointments})

# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_view_rooms_view(request):
#     appointments=models.Appointment.objects.all().filter(status=True)
#     return render(request,'hospital/view_rooms.html',{'appointments':appointments})





# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_appointment_view(request):
#     appointmentForm=forms.AppointmentForm()
#     mydict={'appointmentForm':appointmentForm,}
#     if request.method=='POST':
#         appointmentForm=forms.AppointmentForm(request.POST)
#         if appointmentForm.is_valid():
#             appointment=appointmentForm.save(commit=False)
#             appointment.doctorId=request.POST.get('doctorId')
#             appointment.patientId=request.POST.get('patientId')
#             appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
#             appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
#             appointment.status=True
#             appointment.save()
#         return HttpResponseRedirect('admin-view-appointment')
#     return render(request,'hospital/admin_add_appointment.html',context=mydict)


# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_add_room_view(request):
#     appointmentForm=forms.AppointmentForm()
#     mydict={'appointmentForm':appointmentForm,}
#     if request.method=='POST':
#         appointmentForm=forms.AppointmentForm(request.POST)
#         if appointmentForm.is_valid():
#             appointment=appointmentForm.save(commit=False)
#             appointment.doctorId=request.POST.get('doctorId')
#             appointment.patientId=request.POST.get('patientId')
#             appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
#             appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
#             appointment.status=True
#             appointment.save()
#         return HttpResponseRedirect('admin-view-appointment')
#     return render(request,'hospital/book_room.html',context=mydict)




# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_approve_appointment_view(request):
#     #those whose approval are needed
#     appointments=models.Appointment.objects.all().filter(status=False)
#     return render(request,'hospital/admin_approve_appointment.html',{'appointments':appointments})

# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def admin_approve_rooms_view(request):
#     #those whose approval are needed
#     appointments=models.Appointment.objects.all().filter(status=False)
#     return render(request,'hospital/approve_rooms.html',{'appointments':appointments})




# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def approve_appointment_view(request,pk):
#     appointment=models.Appointment.objects.get(id=pk)
#     appointment.status=True
#     appointment.save()
#     return redirect(reverse('admin-approve-appointment'))



# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
# def reject_appointment_view(request,pk):
#     appointment=models.Appointment.objects.get(id=pk)
#     appointment.delete()
#     return redirect('admin-approve-appointment')
# #---------------------------------------------------------------------------------
# #------------------------ ADMIN RELATED VIEWS END ------------------------------
# #---------------------------------------------------------------------------------






# #---------------------------------------------------------------------------------
# #------------------------ DOCTOR RELATED VIEWS START ------------------------------
# #---------------------------------------------------------------------------------
# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_dashboard_view(request):
#     #for three cards
#     patientcount=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id).count()
#     appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
#     patientdischarged=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

#     #for  table in doctor dashboard
#     appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
#     patientid=[]
#     for a in appointments:
#         patientid.append(a.patientId)
#     patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
#     appointments=zip(appointments,patients)
#     mydict={
#     'patientcount':patientcount,
#     'appointmentcount':appointmentcount,
#     'patientdischarged':patientdischarged,
#     'appointments':appointments,
#     'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
#     }
#     return render(request,'hospital/doctor_dashboard.html',context=mydict)

# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_message_view(request):
#     #for three cards
#     patientcount=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id).count()
#     appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
#     patientdischarged=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name).count()

#     #for  table in doctor dashboard
#     appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
#     patientid=[]
#     for a in appointments:
#         patientid.append(a.patientId)
#     patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid).order_by('-id')
#     appointments=zip(appointments,patients)
#     mydict={
#     'patientcount':patientcount,
#     'appointmentcount':appointmentcount,
#     'patientdischarged':patientdischarged,
#     'appointments':appointments,
#     'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
#     }
#     return render(request,'hospital/doctor-message.html',context=mydict)



# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_patient_view(request):
#     mydict={
#     'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
#     }
#     return render(request,'hospital/doctor_patient.html',context=mydict)



# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_view_patient_view(request):
#     patients=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id)
#     doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
#     return render(request,'hospital/doctor_view_patient.html',{'patients':patients,'doctor':doctor})



# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_view_discharge_patient_view(request):
#     dischargedpatients=models.PatientDischargeDetails.objects.all().distinct().filter(assignedDoctorName=request.user.first_name)
#     doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
#     return render(request,'hospital/doctor_view_discharge_patient.html',{'dischargedpatients':dischargedpatients,'doctor':doctor})



# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_appointment_view(request):
#     doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
#     return render(request,'hospital/doctor_appointment.html',{'doctor':doctor})

# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_message_view(request):
#     doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
#     return render(request,'hospital/doctor_message.html',{'doctor':doctor})

# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_view_appointment_view(request):
#     doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
#     appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
#     patientid=[]
#     for a in appointments:
#         patientid.append(a.patientId)
#     patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
#     appointments=zip(appointments,patients)
#     return render(request,'hospital/doctor_view_appointment.html',{'appointments':appointments,'doctor':doctor})

# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_view_message_view(request):
#     doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
#     appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
#     patientid=[]
#     for a in appointments:
#         patientid.append(a.patientId)
#     patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
#     appointments=zip(appointments,patients)
#     return render(request,'hospital/doctor_view_message.html',{'appointments':appointments,'doctor':doctor})



# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def doctor_delete_appointment_view(request):
#     doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
#     appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
#     patientid=[]
#     for a in appointments:
#         patientid.append(a.patientId)
#     patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
#     appointments=zip(appointments,patients)
#     return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})



# @login_required(login_url='doctorlogin')
# @user_passes_test(is_doctor)
# def delete_appointment_view(request,pk):
#     appointment=models.Appointment.objects.get(id=pk)
#     appointment.delete()
#     doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
#     appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
#     patientid=[]
#     for a in appointments:
#         patientid.append(a.patientId)
#     patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
#     appointments=zip(appointments,patients)
#     return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})



# #---------------------------------------------------------------------------------
# #------------------------ DOCTOR RELATED VIEWS END ------------------------------
# #---------------------------------------------------------------------------------






# #---------------------------------------------------------------------------------
# #------------------------ PATIENT RELATED VIEWS START ------------------------------
# #---------------------------------------------------------------------------------
# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_dashboard_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id)
#     doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
#     mydict={
#     'patient':patient,
#     'doctorName':doctor.get_name,
#     'doctorMobile':doctor.mobile,
#     'doctorAddress':doctor.address,
#     'symptoms':patient.symptoms,
#     'doctorDepartment':doctor.department,
#     'admitDate':patient.admitDate,
#     }
#     return render(request,'hospital/patient_dashboard.html',context=mydict)

# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_message_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id)
#     doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
#     mydict={
#     'patient':patient,
#     'doctorName':doctor.get_name,
#     'doctorMobile':doctor.mobile,
#     'doctorAddress':doctor.address,
#     'symptoms':patient.symptoms,
#     'doctorDepartment':doctor.department,
#     'admitDate':patient.admitDate,
#     }
#     return render(request,'hospital/patient-message.html',context=mydict)

# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_appointment_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     return render(request,'hospital/patient_appointment.html',{'patient':patient})

# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_message_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     return render(request,'hospital/patient_message.html',{'patient':patient})



# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_book_appointment_view(request):
#     appointmentForm=forms.PatientAppointmentForm()
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     message=None
#     mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
#     if request.method=='POST':
#         appointmentForm=forms.PatientAppointmentForm(request.POST)
#         if appointmentForm.is_valid():




#             appointment=appointmentForm.save(commit=False)
#             appointment.doctorId=request.POST.get('doctorId')
#             appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
#             appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
#             appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
#             appointment.status=False
#             appointment.save()
#         return HttpResponseRedirect('patient-view-appointment')
#     return render(request,'hospital/patient_book_appointment.html',context=mydict)


# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_temperature_view(request):
#     appointmentForm=forms.PatientAppointmentForm()
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     message=None
#     mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
#     if request.method=='POST':
#         appointmentForm=forms.PatientAppointmentForm(request.POST)
#         if appointmentForm.is_valid():




#             appointment=appointmentForm.save(commit=False)
#             appointment.doctorId=request.POST.get('doctorId')
#             appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
#             appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
#             appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
#             appointment.status=False
#             appointment.save()
#         return HttpResponseRedirect('patient-temperature')
#     return render(request,'hospital/patients_temperature.html',context=mydict)


# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_message_doctor_view(request):
#     appointmentForm=forms.PatientMessageForm()
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     message=None
#     mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
#     if request.method=='POST':
#         appointmentForm=forms.PatientAppointmentForm(request.POST)
#         if appointmentForm.is_valid():



#             appointment=appointmentForm.save(commit=False)
#             appointment.doctorId=request.POST.get('doctorId')
#             appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
#             appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
#             appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
#             appointment.status=True
#             appointment.save()
#         return HttpResponseRedirect('patient-view-message')
#     return render(request,'hospital/patient_message_doctor.html',context=mydict)




# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_view_appointment_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
#     return render(request,'hospital/patient_view_appointment.html',{'appointments':appointments,'patient':patient})


# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_view_history_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
#     return render(request,'hospital/patient_view_history.html',{'appointments':appointments,'patient':patient})



# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_view_message_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
#     return render(request,'hospital/patient_view_message.html',{'appointments':appointments,'patient':patient})




# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_discharge_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     dischargeDetails=models.PatientDischargeDetails.objects.all().filter(patientId=patient.id).order_by('-id')[:1]
#     patientDict=None
#     if dischargeDetails:
#         patientDict ={
#         'is_discharged':True,
#         'patient':patient,
#         'patientId':patient.id,
#         'patientName':patient.get_name,
#         'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
#         'address':patient.address,
#         'mobile':patient.mobile,
#         'symptoms':patient.symptoms,
#         'admitDate':patient.admitDate,
#         'releaseDate':dischargeDetails[0].releaseDate,
#         'daySpent':dischargeDetails[0].daySpent,
#         'medicineCost':dischargeDetails[0].medicineCost,
#         'roomCharge':dischargeDetails[0].roomCharge,
#         'doctorFee':dischargeDetails[0].doctorFee,
#         'OtherCharge':dischargeDetails[0].OtherCharge,
#         'total':dischargeDetails[0].total,
#         }
#         print(patientDict)
#     else:
#         patientDict={
#             'is_discharged':False,
#             'patient':patient,
#             'patientId':request.user.id,
#         }
#     return render(request,'hospital/patient_discharge.html',context=patientDict)


# #------------------------ PATIENT RELATED VIEWS END ------------------------------
# #---------------------------------------------------------------------------------








# #---------------------------------------------------------------------------------
# #------------------------ ABOUT US AND CONTACT US VIEWS START ------------------------------
# #---------------------------------------------------------------------------------


# # def chat_view(request, pk=None):
# #     appointment = models.Appointment.objects.get(id=pk)
    
# #     if not models.Chat.objects.all().filter(appointment__id=pk).exists():
# #         models.Chat.objects.create(appointment=appointment)
        
# #     chat = models.Chat.objects.get(appointment__id=pk);
    
# #     patient_chats=models.Message.objects.all().filter(chatId=chat).all()

# #     print("\n\n\n")
# #     print(patient_chats)
# #     print("\n\n\n")
    
# #     return render(request,'hospital/chat_page.html', {'messages': patient_chats, 'sender_id': appointment.patientId, 'receiver_id': appointment.doctorId})


# # product search
# def search_disease(request):
#     """ search function  """
#     if request.method == "POST":
#         query_name = request.POST.get('name', None)
#         if query_name:
#             results = models.Disease.objects.filter(name__contains=query_name)
#             return render(request, 'hospital/search.html', {"results":results})

#     return render(request, 'hospital/search.html')



# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
# def patient_symptoms_view(request):
#     patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
#     appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
#     return render(request,'hospital/patient_symptoms.html',{'appointments':appointments,'patient':patient})