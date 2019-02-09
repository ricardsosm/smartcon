from django import forms
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
			cli = kwargs.pop('cli','')
			super(CarteiraNovaForm.gerar, self).__init__(*args, **kwargs)
			self.fields['name']=forms.CharField(label = 'Nome',widget=forms.TextInput(attrs={'value':argu,'readonly':'True'}))
			self.fields['cli']=forms.ModelChoiceField(
				label = 'Cliente',
				queryset=Cliente.objects.filter(id=cli),
				initial=0,
			)

		class Meta:
			model = Carteira
			fields = ['name','id_cliente','public_key','private_key']
