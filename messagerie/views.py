from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def recevoir(request):
    received_messages = Message.objects.filter(recipient=request.user)
    return render(request, 'recevoir.html', {'received_messages': received_messages})

@login_required
def envoyer(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'envoyer.html', {'form': form})
