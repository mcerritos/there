from django.contrib import admin
from .models import Cryptid, Sighting, Power

# Register your models here.
admin.site.register(Cryptid)
admin.site.register(Sighting)
admin.site.register(Power)
