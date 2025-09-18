from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Ansatt, Emne, StudentEmne

# Create your views here.
def index(request):
    studenter = Student.objects.all()
    ansatte = Ansatt.objects.all()
    context = {
        'studenter' : studenter,
        'ansatte' : ansatte
    }
    return render(request, 'app2000/index.html', context)

def emne(request):
    return render(request, 'app2000/emne.html')

def valgtEmne(request):
    if request.method == 'POST':
        emne = request.POST.get('emne')
        info = StudentEmne.objects.filter(emnekode=emne).select_related('student')
        context = {
            'emne' : emne,
            'info' : info
        }
        return render(request, 'app2000/valgtEmne.html', context)

def registrerStudent(request):
    if request.method == 'POST':
        studentnr = request.POST.get('studentnr')
        emnekode = request.POST.get('emnekode')

        student = Student.objects.filter(studentnr=studentnr).first()
        if not student:
            return HttpResponse("Student finnes ikke.")

        emne = Emne.objects.filter(emnekode=emnekode).first()
        if not emne:
            return HttpResponse("Emne finnes ikke.")

        registrer = StudentEmne(emnekode=emne, student=student)
        registrer.save()
        return HttpResponse("Student er registrert.")
    else:
        return HttpResponse("Error?")

