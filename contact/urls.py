from django.urls import path

from .views import contactview

urlpatterns = [
    path('', contactview, name='contact'),
]
