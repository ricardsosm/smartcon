from django.urls import path
from carteira import views

app_name = 'car'

urlpatterns = [
	path('cliente-carteira/',views.carteira_mostrar ,name='carteira'),
	path('cliente-gerar/',views.carteira_gerar ,name='carteira_gerar'),
	path('cliente-salvar/',views.carteira_gerar ,name='carteira_salvar'),
	path('cliente-carterira-apagar/<int:pk>',views.carteira_apagar ,name='carteira_apagar'),
	path('cliente-carteira-mostrar/<int:pk>',views.carteira_amostra,name='carteira_amostra'),
	path('cliente-token-novo/',views.token_novo ,name='token_novo'),
	path('cliente-token-apagar/<int:pk>',views.token_apagar ,name='token_apagar'),

]