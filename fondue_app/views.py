from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
    return HttpResponse("Estou na página de cadastro")


def logar(request):
    return HttpResponse('Estou na página de login')
