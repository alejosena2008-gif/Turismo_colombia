
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('home')

        messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'destinos/login.html')


def registrarse(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirmar_password = request.POST.get('confirmar_password', '')

        if not username or not email or not password:
            messages.error(request, 'Todos los campos son obligatorios.')

        elif password != confirmar_password:
            messages.error(request, 'Las contraseñas no coinciden.')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Este nombre de usuario ya está registrado.')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado.')

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, 'Tu cuenta fue creada correctamente.')
            return redirect('login')

    return render(request, 'destinos/registro.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('home')
