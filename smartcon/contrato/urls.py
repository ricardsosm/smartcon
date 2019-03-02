from django.urls import path
from contrato import views

app_name = 'con'

urlpatterns = [
	path('contrato/',views.contrato ,name='contrato'),
	path('contrato-novo/',views.contrato_novo ,name='contrato_novo'),
	path('contrato-pesquisa/',views.contrato_pesquisa ,name='pescon'),
	path('contrato-apagar/<int:pk>',views.contrato_apaga ,name='delcon'),
	path('contrato-editar/<int:pk>',views.contrato_editar ,name='edicon'),
	path('contrato-mostrar/<int:pk>',views.contrato_mostrar ,name='moscon'),
	path('contrato-pulicar/<int:pk>',views.contrato_puclicar,name='pubcon'),
	path('contrato-recibo/<int:pk>',views.recibo,name='recibo'),
	path('contrato-valrecibo/<int:pk>',views.valrecibo,name='valrecibo'),
]