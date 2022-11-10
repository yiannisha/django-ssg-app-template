from django_distill import distill_path

from .views import get{{ cookiecutter.APP_CLASS_NAME }}View

urlpatterns = [
    distill_path('', get{{ cookiecutter.APP_CLASS_NAME }}View, name='{{ cookiecutter.APP_NAME }}', distill_file='{{ cookiecutter.APP_NAME }}.html'),
]
