import django_filters
from .models import Patient, MedicalRecord, Prescription

class PatientFilter(django_filters.FilterSet):
    
    class Meta:
        model = Patient
        fields = ('id_number',)


class MedicalRecordFilter(django_filters.FilterSet):
    
    class Meta:
        model = MedicalRecord
        fields = ('patient_id',)


class PrescriptionFilter(django_filters.FilterSet):
    class Meta:
        model = Prescription
        fields = ('id_number',)

