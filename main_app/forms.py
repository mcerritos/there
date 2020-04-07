from django import forms
from .models import Cryptid, #Sighting

class CryptidForm(forms.ModelForm):

	class Meta:
		model = Cryptid
		fields = ('name', 'region', 'description', 'danger_level')

# class FeedingForm(forms.ModelForm):

# 	class Meta:
# 		model = Feeding
# 		fields = ['date', 'location', 'description']