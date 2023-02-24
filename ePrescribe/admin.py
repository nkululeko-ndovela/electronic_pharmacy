from django.contrib import admin
from .models import *

admin.site.register(MedPractice)
admin.site.register(Doctor)
admin.site.register(Pharmacy)
admin.site.register(Pharmacist)
admin.site.register(ICD10)
admin.site.register(ActiveIngredients)
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(ContraIndication)
admin.site.register(MedicalInteractions)
admin.site.register(MedicalHistory)
admin.site.register(Reject)
admin.site.register(Dispense)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Suburb)
admin.site.register(Dosage)
admin.site.register(Medication)
admin.site.register(Prescription)

