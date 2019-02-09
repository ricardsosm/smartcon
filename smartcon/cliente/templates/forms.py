from django import forms
from sistema.mail import send_mail_template
from .models  import Cliente
from usuario.models import Usuario
from carteira.models import Carteira
from eth_account import Account



class MostrarCarteira(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
	saldo = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'True'}))
	public_key = forms.CharField(label='Chave Pública',widget=forms.TextInput(attrs={'readonly':'True'}))
	public_key.widget.attrs.update({'size':'40'})  
	private_key = forms.CharField(label='Chave Privada',widget=forms.TextInput(attrs={'readonly':'True'}))
	private_key.widget.attrs.update({'size':'50'}) 

	class Meta:
		model = Carteira
		fields = ['name','saldo','public_key','private_key']

class CarteiraNovaForm(forms.ModelForm):

	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'size':'20'}))	
	public_key = forms.CharField(label='Chave Pública',widget=forms.TextInput(attrs={'readonly':'True'}))
	public_key.widget.attrs.update({'size':'40'})  
	private_key = forms.CharField(label='Chave Privada',widget=forms.TextInput(attrs={'readonly':'True'}))
	private_key.widget.attrs.update({'size':'50'}) 

	class Meta:
		model = Carteira
		fields = ['name','id_cliente','public_key','private_key']

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user','')
		super(CarteiraNovaForm, self).__init__(*args, **kwargs)

		self.fields['id_cliente']=forms.ModelChoiceField(
			label='Cliente',
			queryset=Cliente.objects.filter(id_usuario=user)
		)


	class gerar(forms.ModelForm):

		public_key = forms.CharField(label='Chave Pública',widget=forms.TextInput(attrs={'readonly':'True'}))
		conta = Account.create('KEYSMASHMAX FJAFJKLDSKF7JKFDJ 1530')
		public_key.widget.attrs.update({'value':conta.address}) 
		public_key.widget.attrs.update({'size':'40'})  
		private_key = forms.CharField(label='Chave Privada',widget=forms.TextInput(attrs={'readonly':'True'}))
		private_key.widget.attrs.update({'value':conta.privateKey}) 
		private_key.widget.attrs.update({'size':'50'})
		 
		def __init__(self, *args, **kwargs):
			argu = kwargs.pop('name','')
			cli = kwargs.pop('id_cliente','')
			super(CarteiraNovaForm.gerar, self).__init__(*args, **kwargs)
			self.fields['name']=forms.CharField(label = 'Nome',widget=forms.TextInput(attrs={'value':argu,'readonly':'True'}))
			self.fields['id_cliente']=forms.ModelChoiceField(
				label = 'Cliente',
				queryset=Cliente.objects.filter(id=cli),
				initial=0,
			)

		class Meta:
			model = Carteira
			fields = ['name','id_cliente','public_key','private_key']



@login_required
def carteira_gerar(request):
	template_name = 'carteira_gerar.html'
	carteira = Carteira.objects.all().first()
	context = {}
	form = CarteiraNovaForm(user=request.user.id)
	if request.method == 'POST':
		form = CarteiraNovaForm(user=request.user.id).gerar(name = request.POST["name"],id_cliente = request.POST["id_cliente"])
		if form.is_valid():
			form.save()
			messages.success(request,"Carteira gerada com sucesso",extra_tags='text-success')
			redirect('cli:cliente')
		else:
			messages.success(request,"Errro",extra_tags='text-danger')
			redirect('cli:cliente')			
		#return redirect('cli:cliente')
	context['form'] = form
	return render(request, template_name, context)

