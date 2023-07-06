from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse

def Django_form(request):
    DFO=SingUpForm()
    d={'DFO':DFO}
    if request.method=='POST':
        SUFD=SingUpForm(request.POST)
        if SUFD.is_valid():
            n=SUFD.cleaned_data['name']
            age=SUFD.cleaned_data['age']
            gender=SUFD.cleaned_data['gender']
            return HttpResponse(str(SUFD.cleaned_data))
    return render(request,'django_forms.html',d)