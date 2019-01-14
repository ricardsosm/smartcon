from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'sis'

urlpatterns = [
	path('entrar/',LoginView.as_view(template_name='login.html',redirect_field_name='home.html'),name='login',),
	path('sair/',LogoutView.as_view(template_name= 'home.html' ),name='logout'),
]
