from django.urls import path
from .views import envoyer,recevoir

urlpatterns = [
  path('envoyer/', envoyer, name='envoyer'),
  path('recevoir/', recevoir, name='recevoir'),
]
  