from django import forms
from django.forms import ModelForm
from basicform.models import basicform

class basicform(ModelForm):
    class Meta:
        model = basicform
        fields = '__all__'