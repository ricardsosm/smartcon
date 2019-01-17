from django.urls import path
from usuario import views

app_name = 'usuario'

urlpatterns = [
	path('editar/',views.editar ,name='editar'),
	path('editar_senha/',views.edit_password ,name='editar_senha'),
]
