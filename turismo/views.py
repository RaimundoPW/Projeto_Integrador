from django.shortcuts import render

# Create your views here.
def inicioSite(request):
      return render(request, 'turismo/index.html')
