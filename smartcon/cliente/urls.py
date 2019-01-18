from django.urls import path
from cliente import views

app_name = 'cli'

urlpatterns = [
	path('cliente/',views.cliente ,name='cliente'),
]
