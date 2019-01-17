from django.urls import path
from cliente import views

app_name = 'cli'

urlpatterns = [
	path('painel/',views.painel ,name='painel'),
	path('contrato/',views.contrato ,name='contrato'),
]
