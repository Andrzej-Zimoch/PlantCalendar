from django.shortcuts import render

from .models import Plant
from datetime import datetime, timedelta
from django.http import HttpResponse
from bootstrap_modal_forms.generic import BSModalCreateView,BSModalUpdateView, BSModalDeleteView
from django.urls import reverse_lazy
from .forms import AddPlantForm

# Create your views here.
def base(request):
    plants = Plant.objects.all()

    return render(request,'plant/mastermind.html',{"plants": plants})

def set_date(request):
    plant_id = request.GET['plant_id']
    set_plant = Plant.objects.get(title=plant_id)
    set_plant.first_date= datetime.now()

    set_plant.check_out = set_plant.first_date + timedelta(days=float(set_plant.water_after))

    set_plant.save() 
    
    return HttpResponse("success")

def test(request):
    plants = Plant.objects.all()    
    return render(request,'plant/test.html',{"plants": plants})

class PlantAddView (BSModalCreateView):
    
    template_name = 'plant/create_plant.html'
    form_class = AddPlantForm
    success_message = 'Success: plant was added.'
    success_url = reverse_lazy('base')


class PlantUpdateView(BSModalUpdateView):
    model = Plant
    template_name = 'plant/update_plant.html'
    form_class = AddPlantForm
    success_message = 'Success: plant was updated.'
    success_url = reverse_lazy('base')

class PlantDeleteView(BSModalDeleteView):
    model = Plant
    template_name = 'plant/delete_plant.html'
    success_message = 'Success: plant was deleted.'
    success_url = reverse_lazy('base')