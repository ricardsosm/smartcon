from django.urls import path
from contrato import views

app_name = 'con'

urlpatterns = [
	path('contrato/',views.contrato ,name='contrato'),
	path('contrato-listar/',views.contrato_listar ,name='contrato_listar'),
	path('contrato-pesquisa/',views.contrato_pesquisa ,name='pescon'),
	path('contrato-apagar/<int:pk>',views.contrato_apaga ,name='delcon'),
	path('contrato-editar/<int:pk>',views.contrato_editar ,name='edicon'),
	path('contrato-mostrar/<int:pk>',views.contrato_mostrar ,name='moscon'),
	path('contrato-pulicar/<int:pk>',views.contrato_puclicar,name='pubcon'),
	path('contrato-recibo/<int:pk>',views.recibo,name='recibo'),
	path('contrato-valrecibo/<int:pk>',views.valrecibo,name='valrecibo'),
	path('contrato-interar/<int:pk>',views.contrato_interar,name='intercon'),
	path('contrato-token/',views.contrato_token ,name='contrato_token'),
	path('contrato-distribuir/<int:pk>',views.contrato_distribuir,name='disttoken'),
]