# Generated by Django 5.0.4 on 2024-04-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0026_alter_medicalrecord_date_alter_medicalrecord_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_result',
            name='test_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='test_result',
            name='test_type',
            field=models.CharField(choices=[('Blood', 'Blood'), ('CT Scan', 'CT Scan'), ('Biopsy', 'Biopsy'), ('Imaging', 'Imaging'), ('Colonoscopy', 'Colonoscopy'), ('Blood pressure measurement', 'Blood pressure measurement')], default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='test_result',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]