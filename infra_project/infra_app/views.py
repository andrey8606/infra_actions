from pathlib import Path

from django.shortcuts import render


def index(request):
    print(Path(__file__).resolve().parent.parent)
    return render(request, 'index.html')


def second_page(request):
    return render(request, 'page2.html')
