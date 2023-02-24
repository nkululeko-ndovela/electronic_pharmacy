from django import forms
from .models import *


class MedPracticeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedPracticeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = MedPractice
        fields = ('name', 'address','city','suburb','postal_code','province', 'contact_number', 'email', 'reference')

class DoctorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Doctor
        fields = ('name', 'surname', 'username','password','contact_number', 'email', 'qualification', 'med_practice', 'hc_reg_number')


class DoctorUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoctorUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Doctor
        fields = ('name', 'surname','contact_number', 'email', 'qualification', 'med_practice', 'hc_reg_number')



class PharmacyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PharmacyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pharmacy
        fields = ('name', 'address','city','suburb','postal_code','province', 'contact_number', 'email', 'license_number', 'pharmacist_name')

class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Patient
        fields = ('name', 'surname', 'id_number','username','password', 'address','city','suburb','postal_code','province', 'contact_number', 'email', 'dob','gender')

class PatientUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Patient
        fields = ('name', 'surname', 'id_number','address','city','suburb','postal_code','province', 'contact_number', 'email', 'dob','gender')


class PharmacistForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PharmacistForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pharmacist
        fields = ('name', 'surname', 'username','password','contact_number', 'email', 'reg_number', 'pharmacy')

class PharmacistUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PharmacistUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pharmacist
        fields = ('name', 'surname','contact_number', 'email', 'reg_number', 'pharmacy')


class ActiveIngredientsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActiveIngredientsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ActiveIngredients
        fields = ('name',)

class ICD10Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ICD10Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ICD10
        fields = ('ICD10_code','diagnosis')

class MedicalRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicalRecordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = MedicalRecord
        fields = ('patient_id','disease_id','medication_name','active_ingridients','dosage_form','strength','units','schedule')

class ProvinceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProvinceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Province
        fields = ('name',)

class CityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = City
        fields = ('name','province')

class SuburbForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SuburbForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Suburb
        fields = ('name','postal_code','city')

class DosageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DosageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Dosage
        fields = ('name',)

class MedicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Medication
        fields = ('name','active_ingridients','dosage_form','strength','units','schedule')

class PrescriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Prescription
        fields = ('patient','medication','repeat','quantity','dosage_form','comment')


class PrescriptionUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrescriptionUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Prescription
        fields = ('comment2',)

class PrescriptionRejectUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PrescriptionRejectUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Prescription
        fields = ('comment2',)

class DispenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DispenseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Dispense
        fields = ('pharmacy', 'medical_record', 'contra_indication')

class RejectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RejectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Reject
        fields = ('pharmacy', 'medical_record', 'contra_indication', 'reason')

class MedicalHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicalHistoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = MedicalHistory
        fields = ('patient', 'drug_allergies', 'chronic_med_hist', 'current_chronic_med')