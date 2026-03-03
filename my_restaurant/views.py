from django.shortcuts import render, redirect
from .models import Menu, Reserva

def home(request):
    if request.method == 'POST':
        nome= request.POST.get['nome']
        email= request.POST.get['email']
        data= request.POST.get['data']
        hora= request.POST.get['hora']
        pessoas= request.POST.get['pessoas']
        obs= request.POST.get['obs']

        Reserva.objects.create(
            nome=nome,
            email=email,
            data=data,
            hora=hora,
            pessoas=pessoas,
            observacoes=obs,
        )
        return redirect('home')

    return render (request, 'home.html')

def menu(request):
    pratos = Menu.objects.all()
    return render (request, 'menu.html', {'pratos' : pratos})

def sobre(request):
    return render (request, 'sobre.html')