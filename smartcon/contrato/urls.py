from django.urls import path
from contrato import views

app_name = 'con'

urlpatterns = [
	path('contrato/',views.contrato ,name='contrato'),
	path('contrato-novo/',views.contrato_novo ,name='contrato_novo'),
]