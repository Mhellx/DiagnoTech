from django.shortcuts import redirect

def redirecionar(request):
    return redirect('exames/solicitar_exames/')
