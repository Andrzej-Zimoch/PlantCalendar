
from .models import Plant
from bootstrap_modal_forms.forms import BSModalModelForm

class AddPlantForm(BSModalModelForm):
    
    class Meta:
        model = Plant
        fields = ['title','first_date','water_after','water_ml','photo']
       
