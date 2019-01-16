from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
	
	list_display = ['username','update_at','is_staff']
	search_field = ['name','access']

admin.site.register(Usuario,UsuarioAdmin)
