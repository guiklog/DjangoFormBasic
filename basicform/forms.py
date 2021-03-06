from django import forms
from django.forms import ModelForm
from basicform.models import basicform

class basicform(ModelForm):
    class Meta:
        model = basicform
        fields = '__all__'
        localized_fields = ('phone',)
        
    def checkBoxIsNotTrue(self):
        data = self.cleaned_data['checkbox']
        if data == False:
            raise forms.ValidationError("You must accept to be contacted again to submit the form")

        return data