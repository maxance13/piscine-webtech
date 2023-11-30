from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ('sender', 'recipient', 'subject', 'timestamp', 'is_read')
  list_filter = ('sender', 'recipient', 'timestamp', 'is_read')
  search_fields = ('sender', 'recipient', 'subject', 'body')
  
