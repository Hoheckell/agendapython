from django import forms

from .models import Contato

class PostForm(forms.ModelForm):

	class Meta:
		model = Contato
		fields = ['nome', 'telefone1','telefone2','email','endereco','dtnasc','obs']

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['nome'].widget = forms.TextInput(attrs={
            'id': 'nome',
            'class': 'form-control',
            'name': 'nome',
            'placeholder': 'Nome do contato'})
		self.fields['telefone1'].widget = forms.TextInput(attrs={
            'id': 'telefone1',
            'class': 'form-control',
            'name': 'telefone1',
            'placeholder': 'Primeiro telefone'})
		self.fields['telefone2'].widget = forms.TextInput(attrs={
            'id': 'telefone2',
            'class': 'form-control',
            'name': 'telefone2',
            'placeholder': 'Segundo telefone'})
		self.fields['email'].widget = forms.EmailInput(attrs={
            'id': 'email',
            'class': 'form-control',
            'name': 'email'})
		self.fields['endereco'].widget = forms.Textarea(attrs={
            'id': 'endereco',
            'class': 'form-control',
            'name': 'endereco'})
		self.fields['dtnasc'].widget = forms.DateInput(attrs={
            'id': 'dtnasc',
            'class': 'form-control',
            'name': 'dtnasc',
            'type':'date'})
		self.fields['dtnasc'].localize=True
		self.fields['obs'].widget = forms.Textarea(attrs={
            'id': 'obs',
            'class': 'form-control',
            'name': 'obs'})