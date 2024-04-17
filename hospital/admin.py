from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ExtendedUser)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address','mobile','department']
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
     list_display = ['id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'telephone', 'email', 'ward_village', 'city', 'country']
admin.site.register(Patient, PatientAdmin)

class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'preferred_date', 'preferred_time', 'reason_of_visit','additional_notes']
admin.site.register(AppointmentRequest, AppointmentRequestAdmin)

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor', 'notes', 'medical_history', 'symptoms','diagnosis','prescription',
                    'current_medication','test_results','date','updated_by','updated']
admin.site.register(MedicalRecord, MedicalRecordAdmin)

class TestResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'health_record', 'test_type', 'test_date', 'test_result', 'description','updated_by','updated']
admin.site.register(Test_result, TestResultAdmin)

class MedicalImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'health_record', 'image', 'description', 'updated_by', 'updated_on']
admin.site.register(MedicalImage, MedicalImageAdmin)

class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'health_record', 'treatment', 'start_date', 'end_date', 'updated_by']
admin.site.register(TreatmentPlan, TreatmentPlanAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display = ['id','bill_number', 'patient', 'total_amount', 'date', 'payment_method']
admin.site.register(Bill,BillAdmin)


# class PatientDischargeDetailsAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

# # Register your models here.
# admin.site.register(Disease)
