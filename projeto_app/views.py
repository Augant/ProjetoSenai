from django.shortcuts import render, redirect
from projeto_app.models import Contato


def index(request):
    return render(request, "partial/home.html")


def form(request):
    nome = ''
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data-nascimento')
        if nome and email and data_nascimento:
            print(nome)
            Contato(nome=nome, email=email,
                    data_nascimento=data_nascimento).save()

    return render(request, "partial/form.html", {'nome': nome})

def list(request):
    return render(request, "partial/list.html")
