from django.urls import path
from hospital import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.home_view, name='home'),
    path('patient_department_signup', views.patientdept_signupview, name='patient_dept_signup'),
    path('records_department_signup', views.recordsdept_signupview, name='records_dept_signup'),
    path('finance_department_signup', views.financedept_signupview, name='finance_dept_signup'),
    path('register_patient', views.patient_register, name='register_patient'),
    path('request_appointment', views.request_appointment, name='request_appointment'),
    path('confirmed_appointments', views.confirmed_appointments, name='confirmed_appointments'),
    path('health_records', views.edit_records, name='edit_records'),
    path('medical_records', views.medical_records, name='medical_records'),
    path('test_results', views.test_results, name='test_results'),
    path('medical_image', views.medical_image, name='medical_image'),
    path('treatment_plan', views.treatment_plan, name='treatment_plan'),
    path('view_record',views.view_record, name='view_record'),
    path('billing',views.billing, name='billing'),
    path('patient_dept_create',views.patient_dept_create, name='patient_dept_create'),
    path('records_dept_create',views.records_dept_create, name='records_dept_create'),
    path('financial_dept_create',views.financial_dept_create, name='financial_dept_create'),
    path('home_dashboard1', views.home_dashboard1, name="home_dashboard1"),
    path('home_dashboard2', views.home_dashboard2, name="home_dashboard2"),
    path('home_dashboard3', views.home_dashboard3, name="home_dashboard3"),

#   path('hospital/doctorclick.html', views.doctorclick_view, name='doctorclick'),
#     path('hospital/patientclick.html', views.patientclick_view, name='patientclick'),
#     path('hospital/adminsignup.html', views.admin_signup_view, name='admin_signup'),
#     path('hospital/doctorsignup.html', views.doctor_signup_view, name='doctor_signup_'),
#     path('hospital/patientsignup.html', views.patient_signup_view, name='patient_signup'),
#     path('hospital/patient_wait_for_approval.html', views.afterlogin_view, name='afterlogin_view'),
#     path('hospital/admin_dashboard.html', views.admin_dashboard_view, name='admin_dashboard'),
#     path('hospital/admin_doctor.html', views.admin_doctor_view, name='admin_doctor'),
#     path('hospital/admin_view_doctor.html', views.admin_view_doctor_view, name='admin_view_doctor'),
#     path('candidate_engvote/<str:post_aspired_for>/', views.candidate_engvote, name='candidate_engvote'),
#     path('select_post/', views.select_post, name='select_post'),
#     path('posteng_choice/', views.posteng_choice, name='posteng_choice'),
]

