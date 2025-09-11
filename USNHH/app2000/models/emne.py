from django.db import models
from . import Ansatt

class Emne(models.Model):
    emnekode=models.CharField(max_length=4, primary_key=True)
    foreleser=models.ForeignKey(Ansatt, max_length=6, on_delete=models.PROTECT)
    emnenavn=models.CharField(max_length=40)
    beskrivelse=models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.emnenavn