from django.http import HttpResponse
from django.shortcuts import render
from . models import Clothing

# Create your views here.
def demo(request):
    obj = Clothing.objects.all()
    return render(request, 'index.html', {'result': obj})
