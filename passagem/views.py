from django.shortcuts import render
from passagem.forms import PassagemForms


def index(request):
    form = PassagemForms()
    contexto = {'form' : form}
    return render(request, 'index.html', contexto)
