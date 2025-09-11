from django.db import models
from . import Ansatt
from . import Emne
from. import Student

class Forelesning(models.Model):
    forelesningpk=models.CompositePrimaryKey('dato', 'studentnr', 'emnekode', 'ansattnr')
    studentnr=models.ForeignKey(max_length=6, on_delete=models.PROTECT, null=False, blank=False)
    emnekode=models.ForeignKey(max_length=4, on_delete=models.PROTECT, null=False, blank=False)
    ansattnr=models.ForeignKey(max_length=6, on_delete=models.PROTECT, null=False, blank=False)
    dato=models.DateField()
    beskrivelse=models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.beskrivelse