from django.db import models
from . import Emne, Student, Ansatt

class Forelesning(models.Model):
    emnekode=models.ForeignKey(Emne, max_length=4, on_delete=models.PROTECT, null=False, blank=False)
    student=models.ManyToManyField(Student, through='Forelesningstime', max_length=40)
    foreleser=models.ManyToManyField(Ansatt, through='Forelesningstime', max_length=40)
    beskrivelse=models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.beskrivelse