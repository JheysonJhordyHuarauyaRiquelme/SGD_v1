from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from dojos.models import Dojo  # Asegúrate de importar el modelo Dojo

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.tipo == 'general':
                return redirect('dashboard_general')  # Redirige a la vista del admin general

            elif user.tipo == 'dojo':
                try:
                    # Verifica si el usuario tiene un dojo
                    dojo = Dojo.objects.get(usuario=user)  # Aquí busca si el usuario tiene un dojo
                    return redirect('dashboard_dojo')  # Redirige a la vista del dojo
                except Dojo.DoesNotExist:
                    # Si no tiene dojo, lo redirige a la página de creación de dojo
                    return redirect('crear_dojo')  # Redirige a la vista de crear dojo

        else:
            messages.error(request, 'Usuario o contraseña inválidos.')

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
