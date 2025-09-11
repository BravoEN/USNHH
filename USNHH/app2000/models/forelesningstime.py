from django.db import models
from . import Student, Ansatt, Forelesning

class Forelesningstime(models.Model):
    pk=models.CompositePrimaryKey('dato', 'forelesningsid')
    forelesningsid=models.ForeignKey(Forelesning, on_delete=models.CASCADE, null=False, blank=False)
    ansattnr=models.ForeignKey(Ansatt, max_length=6, on_delete=models.PROTECT, null=False, blank=False)
    studentnr=models.ForeignKey(Student, max_length=6, on_delete=models.PROTECT, null=False, blank=False)
    dato=models.DateField()

    def __str__(self):
        return self.dato