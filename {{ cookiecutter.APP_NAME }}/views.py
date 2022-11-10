import os
from django.shortcuts import render

# Create your views here.
def get{{ cookiecutter.APP_CLASS_NAME }}View (request):
    return render(request, os.path.join('{{ cookiecutter.APP_NAME }}', 'index.html'), {})