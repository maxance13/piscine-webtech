from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('', include('film.urls')),
    path('contact/', include('contact.urls')),
    path('messagerie/', include('messagerie.urls')),
]
