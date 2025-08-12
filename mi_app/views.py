from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Cliente

#Create your views here.
class ClienteView(View):
    @method_decorator(csrf_exempt, name='dispatch')
    def get (self, request):
        Clientes = Cliente.objects.all().values()
        return JsonResponse(list(Clientes), safe=False)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            cliente = cliente.objects.create(
                nombre=data['nombre'],
                apellido=data['apellido'],
                correo=data['correo'],
                telefono=data['telefono'])
            return JsonResponse({"mensaje": "Cliente creado", "id": cliente.nombre})
        except:
            return HttpResponseBadRequest({"Error": "Formato Invalido"})
            
"""
    def get(self, request):
        data = {
            "respuesta": "Hola Mundo"
        }
        return JsonResponse(data)
    
    def post(self, request):
        try:
            body = json.loads(request.body)
        except:
            return HttpResponseBadRequest("Formato Invalido")
        
        data = {
            "status": "ok",
        }

        return JsonResponse(data)
        """

class PaginaView(View):
    def get(self, request):
        return JsonResponse({"mensaje": "Hola desde Paginita"})