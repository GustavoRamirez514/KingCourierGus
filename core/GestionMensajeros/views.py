from django.shortcuts import render
from .models import Mensajeros
from django.views.decorators.http import require_http_methods

# Create your views here.

# listar mensajeros registrados
@require_http_methods(["GET"])
@require_http_methods(["POST"])
def mensajero(request):
    mensajero = Mensajeros.objects.filter(activo=True)
    if mensajero.exists():
        return render(request, 'mensajeros/index.html', {
            'mensajeros': mensajero
        })
    else:
        message = "No hay mensajeros registrados"
        return render(request, 'mensajeros/index.html', {
            'message': message
        })
