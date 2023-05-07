from django.contrib import admin
from api.models import Note
# Register your models here..

    
class NotesAdmin(admin.ModelAdmin):
    list_display=('title','content')
    list_filter=('title',)    

admin.site.register(Note,NotesAdmin)
