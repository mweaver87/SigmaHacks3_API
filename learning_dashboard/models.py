from django.db import models

class Notes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length = 1000)
    subject = models.CharField(max_length = 25)
    file_name = models.CharField(max_length = 100, blank = True, null = True)

class Messages(models.Model):
    text_message = models.TextField(max_length = 250)
    date = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    user = models.TextField(max_length = 25)

    def __str__(self):
        return '%s - %s - %s' % (self.time, self.user, self.text_message)
        
