import datetime

from django.contrib.auth.hashers import make_password
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .filters import PatientFilter, MedicalRecordFilter, PrescriptionFilter
from .forms import *

from .models import *


def admin_view(request):
    return render(request, 'admin_page.html')


# only pharmacist can dispense or reject medication 
class DispenseCreate(LoginRequiredMixin, CreateView): 
    model = Dispense
    form_class = DispenseForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.pharmacist = self.request.user
        return super().form_valid(form)
    
    
class DispenseDetailView(DetailView):
    model = Dispense
    template_name = 'pharmacist/dispense_detail.html'
       
# end of dispensing medication


# rejecting mdication views
class RejectCreate(LoginRequiredMixin, CreateView): 
    model = Reject
    form_class = RejectForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.pharmacist = self.request.user
        return super().form_valid(form)
    
    
class RejectDetailView(DetailView):
    model = Reject
    template_name = 'pharmacist/reject_detail.html'


class RejectListView(ListView):
    model = Reject
    template_name = 'pharmacist/rejected_prescriptions.html'
    context_object_name = 'rejected'
    ordering = ['-date']
    # paginate_by = 12


# medpractice views
# only admin must be able to add med practices
class MedicalHistoryListView(ListView):
    model = MedicalHistory
    template_name = 'MedicalHistory/MedicalHistory.html'
    context_object_name = 'all_MedicalHistory'
    ordering = ['-date']
    # paginate_by = 12
 
  
class MedicalHistoryCreate(LoginRequiredMixin, CreateView): 
    model = MedicalHistory
    form_class = MedicalHistoryForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super().form_valid(form)
    
    
class MedicalHistoryDetailView(DetailView):
    model = MedicalHistory
    template_name = 'MedicalHistory/MedicalHistory_detail.html'
    
    
class MedicalHistoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicalHistory
    form_class = MedicalHistoryForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True



class MedicalHistoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MedicalHistory
    template_name = 'MedicalHistory/confirm_delete.html'
    success_url = reverse_lazy('medhist-list')

    def test_func(self):
        return True
    
    
# end of MedicalHistory views



# medpractice views
# only admin must be able to add med practices
class MedPracticeListView(ListView):
    model = MedPractice
    template_name = 'medpractice/medpractice.html'
    context_object_name = 'all_medpractices'
    ordering = ['-date']
    # paginate_by = 12
 
  
class MedPracticeCreate(LoginRequiredMixin, CreateView): 
    model = MedPractice
    form_class = MedPracticeForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    
    
class MedPracticeDetailView(DetailView):
    model = MedPractice
    template_name = 'medpractice/medpractice_detail.html'
    
    
class MedPracticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedPractice
    form_class = MedPracticeForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True



class MedPracticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MedPractice
    template_name = 'medpractice/confirm_delete.html'
    success_url = reverse_lazy('medprac-list')

    def test_func(self):
        return True
    
# end of medpractice views


# doctor views
# only admin must be able to add med practices
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor/doctor.html'
    context_object_name = 'all_doctors'
    ordering = ['-date']
    # paginate_by = 12
 
  
class DoctorCreate(LoginRequiredMixin, CreateView): 
    model = Doctor
    form_class = DoctorForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        form.instance.practice_number = form.instance.med_practice.reference
        form.instance.password = make_password(form.instance.password)
        UserProfile = User.objects.create(username=form.instance.username,password=form.instance.password,
                            first_name=form.instance.name,last_name=form.instance.surname,is_doctor=True)
        UserProfile.save()
        form.save(commit=True)
        return super().form_valid(form)
    
    
class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor/doctor_detail.html'
    
    
class DoctorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Doctor
    form_class = DoctorUpdateForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        form.instance.password = make_password(form.instance.password)
        UserProfile = User.objects.update(first_name=form.instance.name,last_name=form.instance.surname)
        return super().form_valid(form)

    def test_func(self):
        return True



class DoctorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Doctor
    template_name = 'doctor/confirm_delete.html'
    success_url = reverse_lazy('doctor-list')

    def test_func(self):
        return True
    
# end of Doctor views


# pharmacy views
# only admin must be able to add pharmacies
class PharmacyListView(ListView):
    model = Pharmacy
    template_name = 'pharmacy/pharmacy.html'
    context_object_name = 'all_pharmacy'
    ordering = ['-date']
    # paginate_by = 12
 
  
class PharmacyCreate(LoginRequiredMixin, CreateView): 
    model = Pharmacy
    form_class = PharmacyForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    
    
class PharmacyDetailView(DetailView):
    model = Pharmacy
    template_name = 'pharmacy/pharmacy_detail.html'
    
    
class PharmacyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pharmacy
    form_class = PharmacyForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True



class PharmacyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pharmacy
    template_name = 'pharmacy/confirm_delete.html'
    success_url = reverse_lazy('pharmacy-list')

    def test_func(self):
        return True
    
# end of Pharmacy views

# Pharmacist views
# only admin must be able to add pharmacists
class PharmacistListView(ListView):
    model = Pharmacist
    template_name = 'pharmacist/pharmacist.html'
    context_object_name = 'all_pharmacist'
    ordering = ['-date']
    # paginate_by = 12
 
  
class PharmacistCreate(LoginRequiredMixin, CreateView): 
    model = Pharmacist
    form_class = PharmacistForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        form.instance.password = make_password(form.instance.password)
        UserProfile = User.objects.create(username=form.instance.username,password=form.instance.password,
                            first_name=form.instance.name,last_name=form.instance.surname,is_pharmacist=True)
        UserProfile.save()
        form.save(commit=True)
        return super().form_valid(form)
    
    
class PharmacistDetailView(DetailView):
    model = Pharmacist
    template_name = 'pharmacist/pharmacist_detail.html'
    
    
class PharmacistUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pharmacist
    form_class = PharmacistUpdateForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        form.instance.password = make_password(form.instance.password)
        UserProfile = User.objects.update(first_name=form.instance.name,last_name=form.instance.surname)
        return super().form_valid(form)

    def test_func(self):
        return True



class PharmacistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pharmacist
    template_name = 'pharmacist/confirm_delete.html'
    success_url = reverse_lazy('pharmacist-list')

    def test_func(self):
        return True
    
# end of Pharmacist views

# ICD10 views
# only admin must be able to add ICD10s
class ICD10ListView(ListView):
    model = ICD10
    template_name = 'Configurations/ICD10/ICD10.html'
    context_object_name = 'all_ICD10'
    ordering = ['-date']
    # paginate_by = 12
 
  
class ICD10Create(LoginRequiredMixin, CreateView): 
    model = ICD10
    form_class = ICD10Form
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    
    
    
class ICD10UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ICD10
    form_class = ICD10Form
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True



class ICD10DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ICD10
    template_name = 'Configurations/ICD10/ICD10_confirm_delete.html'
    success_url = reverse_lazy('ICD10-list')

    def test_func(self):
        return True
    
# end of ICD10 views

# ActiveIngredients views
# only admin must be able to add ActiveIngredients
class ActiveIngredientsListView(ListView):
    model = ActiveIngredients
    template_name = 'Configurations/Ingredients/active_ingridients.html'
    context_object_name = 'all_ActiveIngredients'
    ordering = ['-date']
    # paginate_by = 12
 
  
class ActiveIngredientsCreate(LoginRequiredMixin, CreateView): 
    model = ActiveIngredients
    form_class = ActiveIngredientsForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    
    
class ActiveIngredientsDetailView(DetailView):
    model = ActiveIngredients
    template_name = 'Configurations/Ingredients/act_ing_detail.html'
    
    
class ActiveIngredientsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ActiveIngredients
    form_class = ActiveIngredientsForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True



class ActiveIngredientsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ActiveIngredients
    template_name = 'Configurations/Ingredients/act_ing_confirm_delete.html'
    success_url = reverse_lazy('act-ing-list')

    def test_func(self):
        return True
    
# end of ActiveIngredients views


# Patient views
# only admin must be able to add Patient
class PatientListView(ListView):
    model = Patient
    template_name = 'patient/patient.html'
    context_object_name = 'all_patients'
    ordering = ['-date']
    # paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PatientFilter(self.request.GET, queryset=self.get_queryset())
        return context
 
  
class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/registerpatient.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        form.instance.password = make_password(form.instance.password)
        UserProfile = User.objects.create(username=form.instance.username,password=form.instance.password,
                            first_name=form.instance.name,last_name=form.instance.surname,is_patient=True)
        UserProfile.save()
        form.save(commit=True)
        return super().form_valid(form)
    
    
class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'
    
    
class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    form_class = PatientUpdateForm
    template_name = 'patient/registerpatient.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        form.instance.password = make_password(form.instance.password)
        UserProfile = User.objects.update(first_name=form.instance.name,last_name=form.instance.surname)
        return super().form_valid(form)

    def test_func(self):
        return True



class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Patient
    template_name = 'patient/confirm_delete.html'
    success_url = reverse_lazy('patient-list')

    def test_func(self):
        return True
    

# end of Patient views


# MedicalRecord views
# only admin must be able to add MedicalRecord
class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'MedicalRecord/MedicalRecord.html'
    context_object_name = 'all_MedicalRecord'
    ordering = ['-date']
    # paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MedicalRecordFilter(self.request.GET, queryset=self.get_queryset())
        return context
 
  
class MedicalRecordCreate(LoginRequiredMixin, CreateView): 
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    
    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super().form_valid(form)
    
    
class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = 'MedicalRecord/MedicalRecord_detail.html'
    
    
class MedicalRecordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    
    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True



class MedicalRecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MedicalRecord
    template_name = 'MedicalRecord/confirm_delete.html'
    success_url = reverse_lazy('med-rec-list')

    def test_func(self):
        return True
    
    
class MedicalRecordUserListView(ListView):
    model = MedicalRecord
    template_name = 'patient/patient_list.html'
    context_object_name = 'prescriptions'
    # paginate_by = 12

    

    
# end of MedicalRecord views

# ContraIndication views
# only admin must be able to add ContraIndication
class ContraIndicationListView(ListView):
    model = ContraIndication
    template_name = 'ContraIndication/ContraIndication.html'
    context_object_name = 'all_ContraIndication'
    ordering = ['-date']
    # paginate_by = 12
 
  
class ContraIndicationCreate(LoginRequiredMixin, CreateView): 
    model = ContraIndication
    template_name = 'create.html'
    fields = ['patient_id', 'medicine_id', 'exemption', 'start_date']
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    
    
class ContraIndicationDetailView(DetailView):
    model = ContraIndication
    template_name = 'ContraIndication/ContraIndication_detail.html'
    
    
class ContraIndicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ContraIndication
    template_name = 'create.html'
    fields = ['patient_id', 'medicine_id', 'exemption', 'start_date']
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True



class ContraIndicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ContraIndication
    template_name = 'ContraIndication/confirm_delete.html'
    success_url = reverse_lazy('cont-ind-list')

    def test_func(self):
        return True
    
# end of ContraIndication views



# MedicalInteractions views
# only admin must be able to add MedicalInteractions
class MedicalInteractionsListView(ListView):
    model = MedicalInteractions
    template_name = 'MedicalInteractions/MedicalInteractions.html'
    context_object_name = 'all_MedicalInteractions'
    ordering = ['-date']
    # paginate_by = 12
 
  
class MedicalInteractionsCreate(LoginRequiredMixin, CreateView): 
    model = MedicalInteractions
    template_name = 'create.html'
    fields = ['patient_id', 'doctor_id', 'medicine_id1', 'medicine_id2', 'reasons']
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)
    
    
class MedicalInteractionsDetailView(DetailView):
    model = MedicalInteractions
    template_name = 'MedicalInteractions/MedicalInteractions_detail.html'
    
    
class MedicalInteractionsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicalInteractions
    template_name = 'create.html'
    fields = ['patient_id', 'doctor_id', 'medicine_id1', 'medicine_id2', 'reasons']
    
    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True



class MedicalInteractionsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MedicalInteractions
    template_name = 'MedicalInteractions/confirm_delete.html'
    success_url = reverse_lazy('med-int-list')

    def test_func(self):
        return True
    
# end of MedicalInteractions views

class ProvinceListView(ListView):
    model = Province
    template_name = 'Configurations/Province/Province.html'
    context_object_name = 'all_provinces'
    ordering = ['-date']
    # paginate_by = 12


class ProvinceCreate(LoginRequiredMixin, CreateView):
    model = Province
    form_class = ProvinceForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class ProvinceDetailView(DetailView):
    model = Province
    template_name = 'Configurations/Province/Province.html'


class ProvinceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Province
    form_class = ProvinceForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class ProvinceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Province
    template_name = 'Configurations/Province/confirm_delete.html'
    success_url = reverse_lazy('province-list')

    def test_func(self):
        return True

class CityListView(ListView):
    model = City
    template_name = 'Configurations/City/City.html'
    context_object_name = 'all_cities'
    ordering = ['-date']
    # paginate_by = 12


class CityCreate(LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class CityDetailView(DetailView):
    model = City
    template_name = 'Configurations/City/City.html'


class CityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class CityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = City
    template_name = 'Configurations/City/confirm_delete.html'
    success_url = reverse_lazy('city-list')

    def test_func(self):
        return True

class SuburbListView(ListView):
    model = Suburb
    template_name = 'Configurations/Suburb/Suburb.html'
    context_object_name = 'all_suburbs'
    ordering = ['-date']
    # paginate_by = 12


class SuburbCreate(LoginRequiredMixin, CreateView):
    model = Suburb
    form_class = SuburbForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class SuburbDetailView(DetailView):
    model = Suburb
    template_name = 'Configurations/Suburb/Suburb.html'


class SuburbUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Suburb
    form_class = SuburbForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class SuburbDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Suburb
    template_name = 'Configurations/Suburb/confirm_delete.html'
    success_url = reverse_lazy('suburb-list')

    def test_func(self):
        return True

class DosageListView(ListView):
    model = Dosage
    template_name = 'Configurations/Dosage/Dosage.html'
    context_object_name = 'dosages'
    ordering = ['-date']
    # paginate_by = 12


class DosageCreate(LoginRequiredMixin, CreateView):
    model = Dosage
    form_class = DosageForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class DosageDetailView(DetailView):
    model = Dosage
    template_name = 'Configurations/Dosage/Dosage.html'


class DosageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Dosage
    form_class = DosageForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class DosageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Dosage
    template_name = 'Configurations/Dosage/confirm_delete.html'
    success_url = reverse_lazy('dosage-list')

    def test_func(self):
        return True

class MedicationListView(ListView):
    model = Medication
    template_name = 'Configurations/Medication/Medication.html'
    context_object_name = 'all_medications'
    ordering = ['-date']
    # paginate_by = 12


class MedicationCreate(LoginRequiredMixin, CreateView):
    model = Medication
    form_class = MedicationForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class MedicationDetailView(DetailView):
    model = Medication
    template_name = 'Configurations/Medication/Medication.html'


class MedicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Medication
    form_class = MedicationForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class MedicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Dosage
    template_name = 'Configurations/Medication/confirm_delete.html'
    success_url = reverse_lazy('medication-list')

    def test_func(self):
        return True


class PrescriptionListView(ListView):
    model = Prescription
    template_name = 'patient/Prescription/Prescription.html'
    context_object_name = 'all_prescriptions'
    ordering = ['-date']
    # paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PrescriptionFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PrescriptionCreate(LoginRequiredMixin, CreateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        form.instance.id_number = form.instance.patient.id_number
        form.instance.repeat_left = form.instance.repeat
        return super().form_valid(form)


class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'patient/Prescription/Prescription_detail.html'


class PrescriptionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Prescription
    form_class = PrescriptionUpdateForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.pharmacist = Pharmacist.objects.get(admin=self.request.user.pk)
        form.instance.pharmacy = form.instance.pharmacist.pharmacy_id
        form.instance.repeat_left = int(form.instance.repeat_left) - 1
        form.instance.dispensed_date = datetime.date.today()
        form.instance.status = 'dispensed'
        return super().form_valid(form)

    def test_func(self):
        return True

class PrescriptionRejectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Prescription
    form_class = PrescriptionRejectUpdateForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.pharmacist = Pharmacist.objects.get(admin=self.request.user.pk)
        form.instance.pharmacy = form.instance.pharmacist.pharmacy_id
        form.instance.status = 'rejected'
        return super().form_valid(form)

    def test_func(self):
        return True