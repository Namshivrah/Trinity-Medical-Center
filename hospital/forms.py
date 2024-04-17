from email import message
from django import forms
# from django.contrib.auth.models import User
from .models import Patient, AppointmentRequest, MedicalRecord, Test_result, MedicalImage, TreatmentPlan, Bill, ExtendedUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class PatientRegistrationForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'telephone', 'email', 'ward_village', 'city', 'country']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        } 


class AppointmentRequestForm(forms.ModelForm):
    preferred_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    preferred_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = AppointmentRequest
        fields = ['patient', 'doctor', 'preferred_date', 'preferred_time', 'reason_of_visit', 'additional_notes']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'}),
        } 

class MedicalRecordsForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'notes', 'medical_history', 'symptoms', 'diagnosis', 'prescription',
                   'current_medication', 'test_results', 'date', 'updated_by', 'updated']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        } 

class TestResultForm(forms.ModelForm):
    updated = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    test_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    
    class Meta:
        model = Test_result
        fields = ['health_record', 'test_type', 'test_date', 'test_result',  'description',
                    'updated_by', 'updated']
        widgets = {
            'updated': forms.DateInput(attrs={'type': 'date'}),
            'test_date': forms.DateInput(attrs={'type': 'date'}),
        } 

class MedicalImageForm(forms.ModelForm):
    updated_on = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    
    class Meta:
        model = MedicalImage
        fields = ['health_record', 'image', 'description', 'updated_by',  'updated_on']
        widgets = {
            'updated_on': forms.DateInput(attrs={'type': 'date'}),
        } 

class TreatmentPlanForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 

    class Meta:
        model = TreatmentPlan
        fields = ['patient', 'doctor', 'health_record', 'treatment', 'start_date', 'end_date',  'updated_by']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        } 

class BillForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 

    class Meta:
        model = Bill
        fields = ['bill_number', 'patient', 'total_amount', 'date', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        } 



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = ExtendedUser
        fields = ('username', 'email', 'password1', 'password2','department')

class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = ExtendedUser
        fields = ('username', 'password','department')
       

# #for admin signup
# class AdminSigupForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }


# #for student related form
# class DoctorUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model=models.Doctor
#         fields=['address','mobile','department','status','profile_pic']



# #for patient related form
# class PatientUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
# class PatientForm(forms.ModelForm):
#     #this is the extrafield for linking patient and their assigend doctor
#     #this will show dropdown __str__ method doctor model is shown on html so override it
#     #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
#     assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
#     class Meta:
#         model=models.Patient
#         fields=['address','mobile','status','symptoms','profile_pic']



# class AppointmentForm(forms.ModelForm):
#     doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
#     patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
#     class Meta:
#         model=models.Appointment
#         fields=['description','status']


# class PatientAppointmentForm(forms.ModelForm):
#     doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
#     class Meta:
#         model=models.Appointment
#         fields=['description','status']

# class PatientMessageForm(forms.ModelForm):
#     doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
#     class Meta:
#         model=models.Appointment
#         fields=['description','status']


# #for contact us page
# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# # class MessageForm(forms.ModelForm):
# #     # appointment_id
# #     # sender_id
# #     # receiver_id
# #     # chat message
    
# #     appointmentId=forms.ModelChoiceField(queryset=models.Chat.objects.all().filter(appointmentId=True), empty_label="Appointment ID", to_field_name="user_id")
# #     sender_id=forms.ModelChoiceField(queryset=models.Message.objects.all().filter(status=True), empty_label="Sender ID", to_field_name="user_id")
# #     receiver_id=forms.ModelChoiceField(queryset=models.Message.objects.all().filter(status=True), empty_label="Receiver ID", to_field_name="user_id")
# #     class Meta:
# #         model=models.Chat
# #         fields=['message']