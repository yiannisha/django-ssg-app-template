from django.apps import AppConfig


class {{ cookiecutter.APP_CLASS_NAME }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ cookiecutter.APP_NAME }}'
