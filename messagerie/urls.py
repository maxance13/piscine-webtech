from django.urls import path
from .views import envoyer,recevoir,voir

urlpatterns = [
  path('envoyer/', envoyer, name='envoyer'),
  path('', recevoir, name='recevoir'),
  path ('voir/<int:message_id>/', voir, name='voir'),
]
  