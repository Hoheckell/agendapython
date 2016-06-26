from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .forms import PostForm
from .models import Contato
# Create your views here.

def consulta(request):
	contatos = Contato.objects.all()
	return render(request,'agendapp/consulta.html',{'contatos':contatos})

def contato_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			contato = form.save(commit=False)
			contato.telefone1 = request.POST.get('telefone1')
			contato.telefone2 = request.POST.get('telefone2')
			contato.email = request.POST.get('email')
			contato.endereco = request.POST.get('endereco')
			contato.dtnasc = request.POST.get('dtnasc')
			contato.obs = request.POST.get('obs')
			contato.save()
			return redirect('contato_detail', pk=contato.pk)
	else:
		form = PostForm()

    	return render(request, 'agendapp/contato_edit.html', {'form': form})


def contato_edit(request, pk):
	contato = get_object_or_404(Contato, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=contato)
		if form.is_valid():
			contato = form.save(commit=False)
			contato.telefone1 = request.telefone1
			contato.telefone2 = request.telefone2
			contato.email = request.email
			contato.endereco = request.endereco
			contato.dtnasc = request.dtnsac
			contato.obs = request.obs
			contato.save()
			return redirect(views.contato_detail, pk=contato.pk)
	else:
		form = PostForm(instance=contato)

   	return render(request, 'agendapp/contato_edit.html', {'form': form})

def contato_delete(request, pk):
	try:
		contato = get_object_or_404(Contato, pk=pk)
		contato.delete()
		return redirect('/consulta',{'msg':'Contato excluido com sucesso','type':'success'})
	except Exception, err:		
		return redirect('/consulta',{'msg':'ERROR: %sn' % str(err),'type':'error'})

def contato_detail(request, pk):
	contato = get_object_or_404(Contato, pk=pk)
	return render(request, 'agendapp/contato_detail.html', {'contato': contato})