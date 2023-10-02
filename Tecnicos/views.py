from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TecnicoSerializer
from .models import Tecnico 
# Create your views here.

class TecnicoView(viewsets.ModelViewSet):
    serializer_class = TecnicoSerializer
    queryset = Tecnico.objects.all()