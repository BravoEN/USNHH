from django.db import models
from . import Emne, Student

class Forelesning(models.Model):
    pk=models.CompositePrimaryKey('dato', 'emnekode', 'student')
    dato=models.DateField()
    emnekode=models.ForeignKey(Emne, max_length=4, on_delete=models.PROTECT, null=False, blank=False)
    student=models.ForeignKey(Student, on_delete=models.PROTECT, max_length=6,  null=False, blank=False)
    innhold=models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.innhold