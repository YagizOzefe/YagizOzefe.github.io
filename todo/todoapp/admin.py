from django.contrib import admin
from .models import *

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('todo','slug','user')
    search_fields = ('todo',)
    # list_editable = ['todo','slug',]
    # paginator = Paginator


admin.site.register(Todo,TodoAdmin)