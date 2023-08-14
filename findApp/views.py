from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from PIL import *
# Create your views here.

def index(request):
    return redirect('ShowItems')

def insertPage(request):
    return render(request,"insertItems.html")

def insertItems(request):
    if request.method == 'POST':
        image = request.FILES.get('image')  # Use get() to handle missing keys
        name = request.POST.get('name')
        price = request.POST.get('price')
        place = request.POST.get('place')

        if image and name and price and place:  # Check if all fields are present
            new_item = findItem.objects.create(Image=image, Name=name, Price=price, Place=place)
            return redirect('ShowItems')  # Redirect to the same view after insertion

    return HttpResponse(request, 'Set the method to Post')  # Replace 'your_template_name' with your actual template name


def ShowItems(request):
    alldata = findItem.objects.all()
    return render(request,"index.html",{'key':alldata})