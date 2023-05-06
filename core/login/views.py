from django.shortcuts import render, redirect
# crea una cookie de autenticacion
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
# Create your views here.

@login_required
def perfil(request):
    return render(request, 'login/perfil.html')

@require_http_methods(["GET", "POST"])
def login_home(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        print(request.POST)
        print(user)
        if user is None:
            return render(request, 'login/login.html', {
                'error': 'usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('welcome')

@login_required
def log_out(request):
    logout(request)
    return redirect('login')
