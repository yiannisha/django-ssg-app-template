import os
from django.shortcuts import render

# Create your views here.
def getAppView (request):
    return render(request, os.path.join('app', 'index.html'), {})