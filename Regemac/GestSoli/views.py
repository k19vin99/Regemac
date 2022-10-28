from django.shortcuts import render, redirect
from .models import Solicitud
from django.contrib import messages


# Create your views here.

def home(request):
    solicitudesListados = Solicitud.objects.all()
    return render(request, "gestionSolicitudes.html", {"solicitudes": solicitudesListados})

def registrarSolicitud(request):
    codigo = request.POST['txtCodigo']
    cliente = request.POST['txtCliente']
    sucursal = request.POST['txtSucursal']
    direccion = request.POST['txtDireccion']
    solicitante = request.POST['txtSolicitante']
    prioridad = request.POST['numPrioridad']

    solicitud = Solicitud.objects.create(
        codigo=codigo, cliente=cliente, sucursal=sucursal, direccion=direccion, solicitante=solicitante, prioridad=prioridad
        )
    messages.success(request, 'Solicitud Registrada.')
    
    return redirect('/')

def edicionSolicitud(request, codigo):
    solicitud = Solicitud.objects.get(codigo=codigo)
    return render(request, "edicionSolicitud.html", {"solicitud": solicitud})

def editarSolicitud(request):
    codigo = request.POST['txtCodigo']
    cliente = request.POST['txtCliente']
    sucursal = request.POST['txtSucursal']
    direccion = request.POST['txtDireccion']
    solicitante = request.POST['txtSolicitante']
    prioridad = request.POST['numPrioridad']
    
    solicitud = Solicitud.objects.get(codigo=codigo)
    solicitud.cliente = cliente
    solicitud.sucursal = sucursal
    solicitud.direccion = direccion
    solicitud.solicitante = solicitante
    solicitud.prioridad = prioridad
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ()
    
    messages.success(request, 'Solicitud modificada')
    
    return redirect('/')
    


def eliminarSolicitud(request, codigo):
    solicitud = Solicitud.objects.get(codigo=codigo)
    solicitud.delete()
    
    messages.success(request, 'Solicitud eliminada')

    return redirect('/')