from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def recevoir(request):
    if request.user.is_authenticated:
        received_messages = Message.objects.filter(recipient=request.user)
        return render(request, 'messagerie/recevoir.html', {'received_messages': received_messages})
    else :
        return redirect( 'login_view')

@login_required
def envoyer(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('recevoir')
    else:
        form = MessageForm()
    return render(request, 'messagerie/envoyer.html', {'form': form})
  
@login_required
def voir(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    return render(request, 'messagerie/voir.html', {'message': message})
