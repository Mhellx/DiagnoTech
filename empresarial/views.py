from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def gerenciar_clientes(request):
    clientes = User.objects.filter(is_staff=False)
    
    nome_completo = request.GET.get('nome')
    email = request.GET.get('email')
    
    if email:
        clientes.filter(email__contains = email)
        
    if nome_completo:
        clientes.get
    
    return render(request, 'gerenciar_clientes.html', {'clientes': clientes})