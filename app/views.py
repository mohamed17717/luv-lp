from django.shortcuts import render
from django.http import HttpResponse

def homepage(request, name='Batoot'):
  return render(request, 'index.html', {'name': name.title()})
  