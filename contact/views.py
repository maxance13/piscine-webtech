from django.shortcuts import render, redirect
from django.views import View
from .models import Contact

def contactview(request):
    if request.method == 'POST':
        firstName = request.POST.get('prenom')
        lastName = request.POST.get('nom')
        email = request.POST.get('mail')
        content = request.POST.get('message')
        # print(f"----------Data: {firstName}, {lastName}, {email}, {content}")
        if firstName and lastName and email and content:
            contacts = Contact(firstName=firstName, lastName=lastName, email=email, content=content)
            contacts.save()
            # print('-----------Succés')
            return redirect('contact')
    # print('---------------Pas succés')
    return render(request, 'contact/contact.html')