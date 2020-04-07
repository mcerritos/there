from django import forms
from .models import Cryptid, Sighting

class CryptidForm(forms.ModelForm):
	class Meta:
		model = Cryptid
		fields = ('name', 'region', 'description', 'danger_level')

class SightingForm(forms.ModelForm):
	class Meta:
		model = Sighting
		fields = ['date', 'location', 'description']