from django.forms import ModelForm
from django.forms import modelformset_factory
from .models import *



class GameFormSet(ModelForm):
	class Meta:
		model = Game
		fields = '__all__'
