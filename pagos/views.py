# pagos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pago
from .forms import PagoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Vista para listar los pagos
@login_required
def listar_pagos(request):
    # Filtramos los pagos por el dojo del usuario autenticado
    pagos = Pago.objects.filter(dojo=request.user.dojo)
    return render(request, 'pagos/listar_pagos.html', {'pagos': pagos})

# Vista para crear un nuevo pago
@login_required
def crear_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # Asignamos el dojo actual del usuario al nuevo pago
            pago = form.save(commit=False)
            pago.dojo = request.user.dojo  # Asignamos el dojo del usuario autenticado
            pago.save()
            messages.success(request, 'Pago creado con éxito')
            return redirect('listar_pagos')
    else:
        form = PagoForm()
    return render(request, 'pagos/crear_pago.html', {'form': form})

# Vista para editar un pago existente
@login_required
def editar_pago(request, pk):
    dojo = request.user.dojo  # acceso directo al dojo del usuario
    pago = get_object_or_404(Pago, id=pk, dojo=dojo)

    if request.method == 'POST':
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.dojo = dojo  # asegúrate de mantener la relación
            pago.save()
            messages.success(request, 'Pago actualizado con éxito')
            return redirect('listar_pagos')
    else:
        form = PagoForm(instance=pago)

    return render(request, 'pagos/editar_pago.html', {'form': form})

# Vista para eliminar un pago
@login_required
def eliminar_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    if request.method == 'POST':
        pago.delete()
        messages.success(request, 'Pago eliminado con éxito')
        return redirect('lista_pagos')
    return render(request, 'pagos/eliminar_pago.html', {'pago': pago})
