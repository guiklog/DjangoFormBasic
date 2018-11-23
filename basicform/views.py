from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import basicform

# Create your views here.


from django.http import HttpResponse


def index(request):
    
    if request.method == 'POST':
        form = basicform(request.POST)
        if form.is_valid():
            
            form.checkBoxIsNotTrue()
            
            new_contact = form.save()
            
            return HttpResponseRedirect('/form/thanks')
            
    else:
        form = basicform()
    
    
    return render(request, 'basicform/index.html', {'form': form})
    

def thanks(request):

    return render(request, 'basicform/thanks.html')
