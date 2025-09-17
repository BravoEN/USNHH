from django.db import models
from . import Emne, Student

class StudentEmne(models.Model):
    pk=models.CompositePrimaryKey('emnekode', 'student')
    emnekode=models.ForeignKey(Emne, max_length=7, on_delete=models.PROTECT, null=False, blank=False)
    student=models.ForeignKey(Student, on_delete=models.PROTECT, max_length=6,  null=False, blank=False)
    
    def __str__(self):
        return self.emnekode