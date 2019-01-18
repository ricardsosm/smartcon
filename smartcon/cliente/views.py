from django.shortcuts import render

def cliente(request):
	template = 'cliente.html'
	return render(request,template)
	