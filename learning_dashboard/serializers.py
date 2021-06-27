from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializer.ModelSerializer):
    created = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length = 1000)
    subject = models.CharField(max_length = 25)
    file_name = models.CharField(max_length = 100)

    class Meta:
        model = Notes
        fields = ['created', 'notes', 'subject', 'file_name']

class Messages(models.Model):
    text_message = models.TextField(max_length = 250)
    date = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    user = models.TextField(max_length = 25)

    class Meta:
        model = Messages
        fields = ['date', 'time', 'text_messages', 'user']