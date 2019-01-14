from django.contrib import admin
from cliente.models import (Usuario)

class UsuarioAdmin(admin.ModelAdmin):
	
	list_display = ['name','slug','start_date','update_at']
	search_field = ['name','slug']

admin.site.register(Usuario)
