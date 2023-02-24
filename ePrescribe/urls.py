from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_view, name="admin-page"),
    
    # med history urls
    path('MedicalHistory/list/', views.MedicalHistoryListView.as_view(), name='medhist-list'),
    path('MedicalHistory/add/',views.MedicalHistoryCreate.as_view(), name="medhist-create"),
    path('<int:pk>/MedicalHistory/details/', views.MedicalHistoryDetailView.as_view(), name='medhist-detail'),
    path('<int:pk>/MedicalHistory/update/', views.MedicalHistoryUpdateView.as_view(), name='medhist-update'),
    path('<int:pk>/MedicalHistory/delete/', views.MedicalHistoryDeleteView.as_view(), name='medhist-delete'),
    
    
    # medpractice urls
    path('medpractice/list/', views.MedPracticeListView.as_view(), name='medprac-list'),
    path('medpractice/add/',views.MedPracticeCreate.as_view(), name="medprac-create"),
    path('<int:pk>/medpractice/', views.MedPracticeDetailView.as_view(), name='medprac-detail'),
    path('<int:pk>/update_medpractice/', views.MedPracticeUpdateView.as_view(), name='medprac-update'),
    path('<int:pk>/delete_medpractice/', views.MedPracticeDeleteView.as_view(), name='medprac-delete'),
    
    # doctor's urls
    path('doctor/list/', views.DoctorListView.as_view(), name='doctor-list'),
    path('doctor/add/',views.DoctorCreate.as_view(), name="doctor-create"),
    path('<int:pk>/doctor/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('<int:pk>/update_doctor/', views.DoctorUpdateView.as_view(), name='doctor-update'),
    path('<int:pk>/delete_doctor/', views.DoctorDeleteView.as_view(), name='doctor-delete'),

    # pharmacy urls
    path('pharmacy/list/', views.PharmacyListView.as_view(), name='pharmacy-list'),
    path('pharmacy/add/',views.PharmacyCreate.as_view(), name="pharmacy-create"),
    path('<int:pk>/pharmacy/', views.PharmacyDetailView.as_view(), name='pharmacy-detail'),
    path('<int:pk>/update_Pharmacy/', views.PharmacyUpdateView.as_view(), name='pharmacy-update'),
    path('<int:pk>/delete_Pharmacy/', views.PharmacyDeleteView.as_view(), name='pharmacy-delete'),

    # pharmacist urls
    path('pharmacist/dispense/<int:pk>/',views.DispenseCreate.as_view(), name="dispense"),
    path('<int:pk>/dispensed/', views.DispenseDetailView.as_view(), name='dispense-detail'),
    path('pharmacist/reject/<int:pk>/',views.RejectCreate.as_view(), name="reject"),
    path('<int:pk>/rejected/', views.RejectDetailView.as_view(), name='reject-detail'),
    path('rejected_prescriptions/', views.RejectListView.as_view(), name='reject-list'),
    path('pharmacist/list/', views.PharmacistListView.as_view(), name='pharmacist-list'),
    path('pharmacist/add/',views.PharmacistCreate.as_view(), name="pharmacist-create"),
    path('<int:pk>/pharmacist/', views.PharmacistDetailView.as_view(), name='pharmacist-detail'),
    path('<int:pk>/update_Pharmacist/', views.PharmacistUpdateView.as_view(), name='pharmacist-update'),
    path('<int:pk>/delete_Pharmacist/', views.PharmacistDeleteView.as_view(), name='pharmacist-delete'),

    # ICD10 urls
    path('ICD10/list/', views.ICD10ListView.as_view(), name='ICD10-list'),
    path('ICD10/add/',views.ICD10Create.as_view(), name="ICD10-create"),
    path('<int:pk>/update_ICD10/', views.ICD10UpdateView.as_view(), name='ICD10-update'),
    path('<int:pk>/delete_ICD10/', views.ICD10DeleteView.as_view(), name='ICD10-delete'),

    # ActiveIngredients urls
    path('ActiveIngredients/list/', views.ActiveIngredientsListView.as_view(), name='act-ing-list'),
    path('ActiveIngredients/add/',views.ActiveIngredientsCreate.as_view(), name="act-ing-create"),
    path('<int:pk>/ActiveIngredients/', views.ActiveIngredientsDetailView.as_view(), name='act-ing-detail'),
    path('<int:pk>/update_ActiveIngredients/', views.ActiveIngredientsUpdateView.as_view(), name='act-ing-update'),
    path('<int:pk>/delete_ActiveIngredients/', views.ActiveIngredientsDeleteView.as_view(), name='act-ing-delete'),

    # Patient urls
    path('Patient/list/', views.PatientListView.as_view(), name='patient-list'),
    path('Patient/add/',views.PatientCreate.as_view(), name="patient-create"),
    path('<int:pk>/Patient/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('<int:pk>/update_Patient/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('<int:pk>/delete_Patient/', views.PatientDeleteView.as_view(), name='patient-delete'),


    # MedicalRecord urls
    path('MedicalRecord/list/', views.MedicalRecordListView.as_view(), name='med-rec-list'),
    path('MedicalRecord/add/',views.MedicalRecordCreate.as_view(), name="med-rec-create"),
    path('<int:pk>/MedicalRecord/', views.MedicalRecordDetailView.as_view(), name='med-rec-detail'),
    path('<int:pk>/update_MedicalRecord/', views.MedicalRecordUpdateView.as_view(), name='med-rec-update'),
    path('<int:pk>/delete_MedicalRecord/', views.MedicalRecordDeleteView.as_view(), name='med-rec-delete'),

    # ContraIndication urls
    path('ContraIndication/list/', views.ContraIndicationListView.as_view(), name='cont-ind-list'),
    path('ContraIndication/add/',views.ContraIndicationCreate.as_view(), name="cont-ind-create"),
    path('<int:pk>/ContraIndication/', views.ContraIndicationDetailView.as_view(), name='cont-ind-detail'),
    path('<int:pk>/update_ContraIndication/', views.ContraIndicationUpdateView.as_view(), name='cont-ind-update'),
    path('<int:pk>/delete_ContraIndication/', views.ContraIndicationDeleteView.as_view(), name='cont-ind-delete'),



    # MedicalInteractions urls
    path('MedicalInteractions/list/', views.MedicalInteractionsListView.as_view(), name='med-int-list'),
    path('MedicalInteractions/add/',views.MedicalInteractionsCreate.as_view(), name="med-int-create"),
    path('<int:pk>/MedicalInteractions/', views.MedicalInteractionsDetailView.as_view(), name='med-int-detail'),
    path('<int:pk>/update_MedicalInteractions/', views.MedicalInteractionsUpdateView.as_view(), name='med-int-update'),
    path('<int:pk>/delete_MedicalInteractions/', views.MedicalInteractionsDeleteView.as_view(), name='med-int-delete'),

#     province urls
    path('province/list/', views.ProvinceListView.as_view(), name='province-list'),
    path('province/add/', views.ProvinceCreate.as_view(), name="province-create"),
    path('<int:pk>/update_province/', views.ProvinceUpdateView.as_view(), name='province-update'),
    path('<int:pk>/delete_province/', views.ProvinceDeleteView.as_view(), name='province-delete'),

#   city urls
    path('city/list/', views.CityListView.as_view(), name='city-list'),
    path('city/add/', views.CityCreate.as_view(), name="city-create"),
    path('<int:pk>/update_city/', views.CityUpdateView.as_view(), name='city-update'),
    path('<int:pk>/delete_city/', views.CityDeleteView.as_view(), name='city-delete'),

#   suburb urls
    path('suburb/list/', views.SuburbListView.as_view(), name='suburb-list'),
    path('suburb/add/', views.SuburbCreate.as_view(), name="suburb-create"),
    path('<int:pk>/update_suburb/', views.SuburbUpdateView.as_view(), name='suburb-update'),
    path('<int:pk>/delete_suburb/', views.SuburbDeleteView.as_view(), name='suburb-delete'),

#   dosage urls
    path('dosage/list/', views.DosageListView.as_view(), name='dosage-list'),
    path('dosage/add/', views.DosageCreate.as_view(), name="dosage-create"),
    path('<int:pk>/update_dosage/', views.DosageUpdateView.as_view(), name='dosage-update'),
    path('<int:pk>/delete_dosage/', views.DosageDeleteView.as_view(), name='dosage-delete'),

#   medication urls
    path('medication/list/', views.MedicationListView.as_view(), name='medication-list'),
    path('medication/add/', views.MedicationCreate.as_view(), name="medication-create"),
    path('<int:pk>/update_medication/', views.MedicationUpdateView.as_view(), name='medication-update'),
    path('<int:pk>/delete_medication/', views.MedicationDeleteView.as_view(), name='medication-delete'),

#   prescription urls
    path('prescription/list/', views.PrescriptionListView.as_view(), name='prescription-list'),
    path('prescription/add/', views.PrescriptionCreate.as_view(), name="prescription-create"),
    path('<int:pk>/update_prescription/', views.PrescriptionUpdateView.as_view(), name='prescription-update'),
    path('<int:pk>/update_prescription/reject', views.PrescriptionRejectUpdateView.as_view(), name='prescription-updater'),
    path('<int:pk>/prescription/', views.PrescriptionDetailView.as_view(), name='prescription-detail'),
]
