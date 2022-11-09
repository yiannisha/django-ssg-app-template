from django_distill import distill_path

from .views import getAppView

urlpatterns = [
    distill_path('', getAppView, name='app', distill_file='app.html'),
]
