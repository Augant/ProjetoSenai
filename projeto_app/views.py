from django.shortcuts import render, redirect,  get_object_or_404
from projeto_app.models import Contato
from django.http import HttpResponse


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
    query = request.GET.get('q')
    if query:
        contatos = Contato.objects.filter(nome__icontains=query)
    else:
        contatos = Contato.objects.all()

    if request.method == 'POST':  # Checa se a requisição é para deletar
        contato_id = request.POST.get('contato_id')
        contato = get_object_or_404(Contato, id=contato_id)
        contato.delete()
        return redirect('list')

    return render(request, 'partial/list.html', {'contatos': contatos, 'query': query})

def edit(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data-nascimento')
        
        if nome and email and data_nascimento:
            contato.nome = nome
            contato.email = email
            contato.data_nascimento = data_nascimento
            contato.save()
            return redirect('list')
    
    return render(request, 'partial/edit.html', {'contato': contato})