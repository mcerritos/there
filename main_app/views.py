from django.shortcuts import render
from .models import Cryptid

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
	return render(request, 'cryptids/detail.html', {'cryptid': cryptid})
