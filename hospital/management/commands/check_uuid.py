from django.core.management.base import BaseCommand
from hospital.models  import Patient
import uuid


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

class Command(BaseCommand):
    help = 'Checks the validity of UUIDs in the Patient model'

    def handle(self, *args, **options):
        for patient in Patient.objects.all():
            if not is_valid_uuid(patient.id):  # replace 'uuid_field' with the name of your UUID field
                self.stdout.write(f"Invalid UUID: {patient.id}")