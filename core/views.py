from django.http import HttpResponse
from django.shortcuts import render
from Persona.models import Persona
from portfolio.models import portfolio as port

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):

    personas = Persona.objects.all()

    return render(request, 'core/contact.html', {
        'personas': personas
    })

def portfolio_view(request):
    portfolio = port.objects.all()
    return render(request, 'core/portfolio.html', {'portfolio': portfolio})
