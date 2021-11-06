from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path


def index(request):
    print(Path(__file__).resolve().parent.parent)
    return render(request, 'index.html')


def second_page(request):
    return render(request, 'page2.html')
