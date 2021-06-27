from django.contrib import admin
from .models import Notes, Messages

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_filter = ('created', 'subject')
    list_display = ('created', 'notes', 'subject')


admin.site.register(Notes, NotesAdmin)
admin.site.register(Messages)