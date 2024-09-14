from django.shortcuts import render, redirect
from django.contrib import messages
from .form import ContatoForm

def criar_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            messages.success(request, 'Contato criado com sucesso!')
            return redirect('partial/home.html')  # Redireciona para o mesmo formulário
        else:
            messages.error(request, 'Não foi possível criar o contato. Verifique os dados e tente novamente.')
    else:
        form = ContatoForm()  # Cria uma instância vazia do formulário

    return render(request, 'partial/form.html', {'form': form})

def index(request):
    return render(request, "partial/home.html")


def form(request):
    return render(request, "partial/form.html")


def list(request):
    return render(request, "partial/list.html")
