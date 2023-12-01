from django.shortcuts import render, redirect
from django.views import View
from .models import Contact

class ContactView(View):
    def get(self, request):
        return render(request, 'contact/contact.html', {'message_sent': False})
    def post(self, request):
        firstName = request.POST.get('prenom')
        lastName = request.POST.get('nom')
        email = request.POST.get('mail')
        content = request.POST.get('message')
        if firstName and lastName and email and content:
            contacts = Contact(firstName=firstName, lastName=lastName, email=email, content=content)
            contacts.save()
            return render(request, 'contact/contact.html', {'message_sent': True})
        return render(request, 'contact/contact.html', {'message_sent': False})
