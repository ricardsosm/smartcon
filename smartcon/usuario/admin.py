from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
	
	list_display = ['username','date_joined','update_at','is_staff']
	search_field = ['name','access']
	exclude = ('password',)

admin.site.register(Usuario,UsuarioAdmin)
