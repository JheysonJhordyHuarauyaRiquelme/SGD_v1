# alumnos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .forms import AlumnoForm
from django.contrib.auth.decorators import login_required

# Vista para listar alumnos del dojo
@login_required
def listar_alumnos(request):
    alumnos = Alumno.objects.filter(dojo=request.user.dojo)
    return render(request, 'alumnos/listar_alumnos.html', {'alumnos': alumnos})

# Vista para crear un alumno
@login_required
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.dojo = request.user.dojo  # Asociar al dojo del usuario
            alumno.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/crear_alumno.html', {'form': form})

# Vista para editar un alumno
@login_required
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, dojo=request.user.dojo)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/editar_alumno.html', {'form': form, 'alumno': alumno})

# Vista para eliminar un alumno
@login_required
def eliminar_alumno(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    alumno.delete()
    return redirect('listar_alumnos')
