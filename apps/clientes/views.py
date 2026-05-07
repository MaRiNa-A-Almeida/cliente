from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ClienteForm
from .models import Cliente

def novo_cliente(request):
    clientes = Cliente.objects.all() # SELECT * FROM clientes
    template_name = 'novo_cliente.html'
    context = {}
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novo_cliente')  # Redireciona para a mesma página após salvar
        else:
            return HttpResponse('<h1>Deu erro no teu formulário<h1>')
        
    form = ClienteForm()
    context['form'] = form
    context['clientes'] = clientes

    return render(request, template_name, context)

def atualizar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        return HttpResponse('<h1>Cliente não encontrado')

    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('novo_cliente')  
        else:
         return HttpResponse('<h1>Erro na atualização do cliente<h1>')

    form = ClienteForm(instance=cliente)
    template_name = 'novo_cliente.html'
    cliente = Cliente.objects.all()
    context = {
    'form': form,
    'clientes': cliente
    }
    return render(request, template_name, context)

def excluir_cliente(request, id):
    try: 
     cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        return HttpResponse('<h1>Erro ao excluir.Cliente não encontrado<h1>')
    return redirect('novo_cliente')
    