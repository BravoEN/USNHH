from django.db import models

class Student(models.Model):
    studentnr=models.CharField(max_length=5, primary_key=True) 
    fornavn=models.CharField(max_length=40)
    etternavn=models.CharField(max_length=40)

    def __str__(self):
        return self.studentnr