from django.contrib import admin
from NormalizeDatabase.models import RawData, Hospitals, HospitalExpenses, HospitalWorkers

# Register your models here.
admin.site.register(RawData)
admin.site.register(Hospitals)
admin.site.register(HospitalExpenses)
admin.site.register(HospitalWorkers)