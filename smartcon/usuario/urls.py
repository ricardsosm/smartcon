from django.urls import path
from usuario import views

app_name = 'usuario'

urlpatterns = [
	path('editar/',views.editar ,name='editar'),
	path('editar-senha/',views.edit_password ,name='editar_senha'),
	path('nova-senha/',views.password_reset ,name='nova_senha'),
	path('confirmar_nova_senha/<key>/',views.password_reset_confirm ,name='reset_senha'),
]
