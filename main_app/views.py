from django.shortcuts import render, redirect
from .models import Cryptid
from .forms import SightingForm

# Create your views here.
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def cryptids_index(request):
	cryptids = Cryptid.objects.all()
	return render(request, 'cryptids.html', {'cryptids': cryptids})

def cryptids_detail(request, cryptid_id):
	cryptid = Cryptid.objects.get(id=cryptid_id)

	sighting_form = SightingForm()
	return render(request, 'cryptids/detail.html', {
		'cryptid': cryptid, 'sighting_form': sighting_form
		})

def add_sighting(request, cryptid_id):
	form = SightingForm(request.POST)
	if form.is_valid():
		new_sighting = form.save(commit=False)
		new_sighting.cryptid_id = cryptid_id
		new_sighting.save()
	return redirect('detail', cryptid_id=cryptid_id)