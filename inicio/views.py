from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.

def inicio(request):
     return render(request, 'inicio.html')

def demo(request):
     return render(request, 'demo.html')