# dojos/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DojoForm
from django.contrib import messages
from dojos.models import Dojo  # Asegúrate de tener el modelo Dojo

@login_required
def crear_dojo(request):
    if request.user.tipo != 'dojo':
        return redirect('dashboard_general')  # Si no es un admin dojo, redirigir

    if request.method == 'POST':
        form = DojoForm(request.POST)
        if form.is_valid():
            dojo = form.save(commit=False)
            dojo.usuario = request.user  # Asignar el dojo al usuario logueado
            dojo.save()
            messages.success(request, 'Dojo creado exitosamente.')
            return redirect('dashboard_dojo')  # Redirigir a la vista del dojo

    else:
        form = DojoForm()

    return render(request, 'dojos/crear_dojo.html', {'form': form})

@login_required
def dashboard_dojo(request):
    # Obtener el dojo asociado al usuario actual (AdminDojo)
    try:
        dojo = Dojo.objects.get(usuario=request.user)
        context = {
            'dojo': dojo,
            'message': f'Bienvenido al Dashboard de tu Dojo: {dojo.nombre}',
        }
    except Dojo.DoesNotExist:
        context = {
            'message': 'No tienes un dojo asignado.',
        }

    return render(request, 'dojos/dashboard_dojo.html', context)

@login_required
def dashboard_general(request):
    # Aquí puedes agregar datos que desees mostrar en el dashboard del admin general
    # Ejemplo: estadísticas, listado de dojos, etc.
    
    # Para este ejemplo, agregamos un mensaje de bienvenida
    context = {
        'user': request.user,
        'message': 'Bienvenido al Dashboard General.',
    }

    return render(request, 'general/dashboard_general.html', context)
