from django.db import models

class Emne(models.Model):
    emnekode=models.CharField(max_length=4, primary_key=True)
    emnenavn=models.CharField(max_length=40)

    def __str__(self):
        return self.emnenavn