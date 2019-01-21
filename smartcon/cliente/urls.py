from django.urls import path
from cliente import views

app_name = 'cli'

urlpatterns = [
	path('cliente/',views.cliente ,name='cliente'),
	path('cliente-novo/',views.cliente_novo ,name='cliente-novo'),
	path('cliente-editar/<int:pk>',views.cliente_editar ,name='cliente_editar'),
]
