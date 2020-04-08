from django.shortcuts import render, redirect
from .models import Cryptid, Sighting, Power
from .forms import SightingForm, CryptidForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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
	unconfirmed_powers = Power.objects.exclude(id__in = cryptid.powers.all().values_list('id'))
	sighting_form = SightingForm()
	return render(request, 'cryptids/detail.html', {
		'cryptid': cryptid, 'sighting_form': sighting_form, 
		'powers': unconfirmed_powers
		})

def assoc_power(request, cryptid_id, power_id):
	Cryptid.objects.get(id=cryptid_id).powers.add(power_id)
	return redirect('detail', cryptid_id=cryptid_id)

def add_cryptid(request):
	if request.method == 'POST':
		form = CryptidForm(request.POST)
		if form.is_valid():
			new_Cryptid = form.save()
			return redirect('index')
	else:
		form = CryptidForm
	context = {'form': form}
	return render(request, 'cryptids/add_cryptid.html', context)


def add_sighting(request, cryptid_id):
	form = SightingForm(request.POST)
	if form.is_valid():
		new_sighting = form.save(commit=False)
		new_sighting.cryptid_id = cryptid_id
		new_sighting.save()
	return redirect('detail', cryptid_id=cryptid_id)


# views for powers
class PowerList(ListView):
	model= Power

class PowerDetail(DetailView):
	model= Power

class PowerCreate(CreateView):
	model= Power
	fields= '__all__'

class PowerUpdate(UpdateView):
	model= Power
	fields = ['name', 'description']

class PowerDelete(DeleteView):
	model = Power
	success_url= '/powers/'