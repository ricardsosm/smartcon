from django.urls import path
from cliente import views

app_name = 'cli'

urlpatterns = [
	path('cliente/',views.cliente ,name='cliente'),
	path('cliente-novo/',views.cliente_novo ,name='cliente-novo'),
	path('cliente-editar/<int:pk>',views.cliente_editar ,name='cliente_editar'),
	path('cliente-mostrar/<int:pk>',views.cliente_mostrar ,name='cliente_mostrar'),
	path('cliente-apagar/<int:pk>',views.cliente_apagar ,name='cliente_apagar'),
	path('cliente-pesquisa/',views.cliente_pesquisa ,name='pescli'),
	path('cliente-carteira/',views.carteira_mostrar ,name='carteira'),
	path('cliente-gerar/',views.carteira_gerar ,name='carteira_gerar'),
	path('cliente-salvar/',views.carteira_gerar ,name='carteira_salvar'),
	path('cliente-carterira-apagar/<int:pk>',views.carteira_apagar ,name='carteira_apagar'),
	path('cliente-carteira-mostrar/<int:pk>',views.carteira_amostra,name='carteira_amostra'),
]