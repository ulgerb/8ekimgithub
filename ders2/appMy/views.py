from django.shortcuts import render
from appMy.models import Constraction
# Create your views here.


def index(request):
    projeler = Constraction.objects.all()
    
    context = {
        "projeler":projeler,
    }
    return render(request,'index.html',context)