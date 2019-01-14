from django.contrib import admin
from cliente.models import (Cliente)

class ClienteAdmin(admin.ModelAdmin):
	
	list_display = ['name','create_at','update_at']
	search_field = ['name']

admin.site.register(Cliente)
