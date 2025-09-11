from django.contrib import admin
from .models import Ansatt, Emne, Student, Forelesning

# Register your models here.
admin.site.register(Ansatt)
admin.site.register(Student)
admin.site.register(Emne)