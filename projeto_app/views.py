from django.shortcuts import render

def index(request):
    return render(request, "partial/home.html")

def form(request):
    return render(request, "partial/form.html")


def list(request):
    return render(request, "partial/list.html")