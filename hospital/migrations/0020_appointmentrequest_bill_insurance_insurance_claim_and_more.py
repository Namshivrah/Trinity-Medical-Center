# Generated by Django 5.0.4 on 2024-04-11 15:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_disease'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentRequest',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('preferred_date', models.DateField(auto_now=True)),
                ('preferred_time', models.TimeField(default='00:00')),
                ('reason_of_visit', models.TextField()),
                ('additional_notes', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'appointment requests',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bill_number', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField(auto_now=True)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Insurance', 'Insurance'), ('Mobile money', 'Mobile money'), ('Bank', 'Bank')], default='Cash', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'bills',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=100)),
                ('coverage_start_date', models.DateTimeField(auto_now=True)),
                ('coverage_end_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'insurances',
            },
        ),
        migrations.CreateModel(
            name='Insurance_Claim',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('claim_number', models.CharField(max_length=100)),
                ('claim_date', models.DateTimeField(auto_now=True)),
                ('claim_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('claim_status', models.CharField(default='pending', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'insurance claims',
            },
        ),
        migrations.CreateModel(
            name='Insurance_Company',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'insurance companies',
            },
        ),
        migrations.CreateModel(
            name='MedicalImage',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='medical_images/')),
                ('description', models.TextField()),
                ('updated_by', models.CharField(default='Test User', max_length=50)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'medical images',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('notes', models.TextField()),
                ('medical_history', models.TextField()),
                ('symptoms', models.TextField()),
                ('diagnosis', models.TextField()),
                ('prescription', models.TextField()),
                ('current_medication', models.TextField()),
                ('test_results', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(default='Test User', max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'medical records',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('read_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('read_status', models.CharField(default='unread', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='Test_result',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('test_type', models.CharField(max_length=100)),
                ('test_date', models.DateTimeField(auto_now=True)),
                ('test_result', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('updated_by', models.CharField(default='Test User', max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'test results',
            },
        ),
        migrations.CreateModel(
            name='TreatmentPlan',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('treatment', models.TextField()),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(default='Test User', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'treatment plans',
            },
        ),
        migrations.DeleteModel(
            name='Disease',
        ),
        migrations.DeleteModel(
            name='PatientDischargeDetails',
        ),
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name_plural': 'appointments'},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name_plural': 'doctors'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name_plural': 'patients'},
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='appointmentDate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='admitDate',
            new_name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctorId',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctorName',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patientId',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patientName',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='status',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='address',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='assignedDoctorId',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='status',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='symptoms',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='reason_of_visit',
            field=models.TextField(default='No reason provided'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(default='No name provided', max_length=50),
        ),
        migrations.AddField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(default='No name provided', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(default='Kampala', max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='country',
            field=models.CharField(default='Uganda', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='No name provided', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=' ', max_length=6),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='No name provided', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='telephone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='ward_village',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='incomplete', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='appointmentrequest',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor'),
        ),
        migrations.AddField(
            model_name='appointmentrequest',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='bill',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='policy_holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='insurance_claim',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.bill'),
        ),
        migrations.AddField(
            model_name='insurance_claim',
            name='insurance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.insurance'),
        ),
        migrations.AddField(
            model_name='insurance_claim',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='insurance_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.insurance_company'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='medicalimage',
            name='health_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.medicalrecord'),
        ),
        migrations.AddField(
            model_name='message',
            name='Recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='notification',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='test_result',
            name='health_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.medicalrecord'),
        ),
        migrations.AddField(
            model_name='treatmentplan',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor'),
        ),
        migrations.AddField(
            model_name='treatmentplan',
            name='health_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.medicalrecord'),
        ),
        migrations.AddField(
            model_name='treatmentplan',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
    ]
