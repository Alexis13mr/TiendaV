from django.http import HttpResponse
from django.shortcuts import render
from .models import item
# Create your views here.

def inicio (request):
    product=item.objects.all()
    return render(request, 'inic.html',{'prod':product})
