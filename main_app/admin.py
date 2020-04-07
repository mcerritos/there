from django.contrib import admin
from .models import Cryptid, Sighting

# Register your models here.
admin.site.register(Cryptid)
admin.site.register(Sighting)
