from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import timedelta

# ----------------------Extended User-------------

class ExtendedUser(User):
    DEPARTMENT_CHOICES = [
        ('Patient Management', 'Patient Management'),
        ('Records Management', 'Records Management'),
        ('Financial Management', 'Financial Management'),
    ]

    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, default='')
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    user_types = [
        ('Patient', 'Patient'),
        ('Records', 'Records'),
        ('Finance', 'Finance'),
    ]

    user_type = models.CharField(max_length=50, choices=user_types, default='')


# -----------PATIENT MANAGEMENT DEPARTMENT-----------
departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    first_name = models.CharField(max_length=50, default='No name provided')
    last_name = models.CharField(max_length=50, default='No name provided')
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')

    # def __str__(self):
    #     return f'First Name: {self.first_name}, Last Name: {self.last_name}'
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "doctors"

GENDERS = [
    ('Male', 'Male'),
    ('Female', 'Female')
]
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    first_name = models.CharField(max_length=50, default='No name provided')
    last_name = models.CharField(max_length=50, default='No name provided')
    gender = models.CharField(max_length=6, choices=GENDERS, default=' ')
    date_of_birth = models.DateField()
    telephone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    ward_village = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, default='Kampala')
    country = models.CharField(max_length=50, default='Uganda')

    # def __str__(self):
    #     return f'First Name: {self.first_name}, Last Name: {self.last_name}, DOB: {self.date_of_birth}'

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
       
    @property
    def patient_details(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'sex': self.gender,
            'dob': self.date_of_birth,
            'telephone': self.telephone,
            'email': self.email,
        }

    class Meta:
        verbose_name_plural = "patients"


class AppointmentRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    reason_of_visit = models.TextField()
    additional_notes = models.TextField()

    def __str__(self):
        return f'Patient: {self.patient}, Doctor: {self.doctor}, Date: {self.preferred_date}, Time: {self.preferred_time}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # Check whether appointment already exists
        
        existing_appointment = Appointment.objects.filter(request=self).first()
        if existing_appointment:
            # If an Appointment already exists, don't create a new one.
            return

        # Check if the preferred_time is available.
        # This is a simple example that checks if there are any Appointments that overlap with the preferred_time.
        # You might need to adjust this based on your specific needs.
        overlapping_appointments = Appointment.objects.filter(
            date=self.preferred_date,
            start_time__lt=self.preferred_time + timedelta(hours=1.5),
            end_time__gt=self.preferred_time
        )
        if overlapping_appointments.exists():
            # If the preferred_time is not available, don't create an Appointment.
            return

        # If there's no existing Appointment and the preferred_time is available, create an Appointment.
        appointment = Appointment.objects.create(
            date=self.preferred_date,
            request=self,
            start_time=self.preferred_time,
            end_time=self.preferred_time + timedelta(hours=1.5),  # Assuming the appointment lasts 1.5 hours.
            status='Confirmed'  # Or calculate the status based on some criteria.
        )
        appointment.save()

    class Meta:
        verbose_name_plural = "appointment requests"


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    request = models.ForeignKey(AppointmentRequest, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=100)
  
    def __str__(self):
        return f'Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}'

    class Meta:
        verbose_name_plural = "appointments"


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    sender = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Recipient = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    body=models.TextField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True)
    read_status=models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class Notification(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    read_status = models.CharField(max_length=50, default='unread')

    def __str__(self):
        return f'Patient: {self.patient}, Date: {self.timestamp}'

    class Meta:
        verbose_name_plural = "notifications"



# ---------------MEDICAL RECORDS DEPARTMENT----------------
class MedicalRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    notes = models.TextField()
    medical_history = models.TextField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    prescription = models.TextField()
    current_medication = models.TextField()
    test_results = models.TextField()
    date = models.DateField()
    updated_by = models.CharField(max_length=50, default='Test User')
    updated = models.DateTimeField()

    def __str__(self):
        return f'Patient: {self.patient}, Doctor: {self.doctor}, Date: {self.date}'

    class Meta:
        verbose_name_plural = "medical records"


TYPE = [
    ('Blood', 'Blood'),
    ('CT Scan', 'CT Scan'),
    ('Biopsy', 'Biopsy'),
    ('Imaging', 'Imaging'),
    ('Colonoscopy', 'Colonoscopy'),
    ('Blood pressure measurement', 'Blood pressure measurement')
]
class Test_result(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    health_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50, choices=TYPE, default=' ')
    test_date = models.DateTimeField()
    test_result = models.CharField(max_length=100)
    description = models.TextField()
    updated_by = models.CharField(max_length=50, default='Test User')
    updated = models.DateTimeField()

    def __str__(self):
        return f'Test Result: {self.test_result}, Test Type: {self.test_type}, health Record: {self.health_record}'

    class Meta:
        verbose_name_plural = "test results"

class MedicalImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    health_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='medical_images/')
    description = models.TextField()
    updated_by = models.CharField(max_length=50, default='Test User')
    updated_on = models.DateTimeField()

    def __str__(self):
        return f'Health Record: {self.health_record}, Image: {self.image}'

    class Meta:
        verbose_name_plural = "medical images"

class TreatmentPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    health_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    treatment = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    updated_by = models.CharField(max_length=50, default='Test User')

    def __str__(self):
        return f'Patient: {self.patient}, Doctor: {self.doctor}, Health Record: {self.health_record}'

    class Meta:
        verbose_name_plural = "treatment plans"



# ---------------BILLING DEPARTMENT----------------
METHOD=[('Cash','Cash'),
('Insurance','Insurance'),
('Mobile money','Mobile money'),
('Bank','Bank'),
]
class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    bill_number = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    payment_method = models.CharField(max_length=50,choices=METHOD,default='Cash')

    def __str__(self):
        return f'Patient: {self.patient}, Total: {self.total_amount}'

    class Meta:
        verbose_name_plural = "bills"

class Insurance_Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f'Name: {self.name}, Address: {self.address}, Contact: {self.contact}'

    class Meta:
        verbose_name_plural = "insurance companies"

class Insurance(models.Model):
    insurance_company = models.ForeignKey(Insurance_Company, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=100)
    policy_holder = models.ForeignKey(Patient, on_delete=models.CASCADE)
    coverage_start_date = models.DateTimeField(auto_now=True)
    coverage_end_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Patient: {self.patient}, Insurance Company: {self.insurance_company}, Policy Number: {self.policy_number}'

    class Meta:
        verbose_name_plural = "insurances"

class Insurance_Claim(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    claim_number = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    claim_date = models.DateTimeField(auto_now=True)
    claim_amount = models.DecimalField(max_digits=6, decimal_places=2)
    claim_status = models.CharField(max_length=50, default='pending')
    
    def __str__(self):
        return f'Insurance: {self.insurance}, Bill: {self.bill}, Claim Amount: {self.claim_amount}'

    class Meta:
        verbose_name_plural = "insurance claims"