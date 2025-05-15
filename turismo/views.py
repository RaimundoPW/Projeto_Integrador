from django.shortcuts import render
from .models import PacoteTuristico

# Create your views here.
def inicioSite(request):
      pacotes = PacoteTuristico.objects.all()
      return render(request, 'turismo/index.html', {'pacotes':pacotes})


