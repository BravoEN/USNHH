from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('emne/', views.emne, name='emne'),
    path('emne/sys1000/', views.valgtEmne, name='sys1000'),
    path('emne/pro1000/', views.valgtEmne, name='pro1000'),
    path('emne/sys1000/registrerStudent', views.registrerStudent, name='registrerStudent'),
    path('emne/pro1000/registrerStudent', views.registrerStudent, name='registrerStudent')
]