from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('cryptids/', views.cryptids_index, name="index"),
	path('cryptids/<int:cryptid_id>/', views.cryptids_detail, name='detail'),
	path('cryptids/add_cryptid/', views.add_cryptid, name='add_cryptid'),
	path('cryptids/<int:cryptid_id>/add_sighting/', views.add_sighting, name='add_sighting'),
	# powers below
	path('powers/', views.PowerList.as_view(), name='powers_index'),
	path('powers/<int:pk>/', views.PowerDetail.as_view(), name='powers_detail'), 
	path('powers/create/', views.PowerCreate.as_view(), name='power_create'), 
	path('powers/<int:pk>/update', views.PowerUpdate.as_view(), name = 'power_update'),
	path('powers/<int:pk>/delete', views.PowerDelete.as_view(), name='power_deleted'),
	path('cryptids/<int:cryptid_id>/assoc_power/<int:power_id>/', views.assoc_power, name='assoc_power'),
]