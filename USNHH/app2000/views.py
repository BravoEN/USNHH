from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Ansatt, Emne, Forelesning

# Create your views here.
def index(request):
    studenter = Student.objects.all()
    context = {'studenter' : studenter}
    return render(request, 'index.html', context)