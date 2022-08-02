from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login

from accounts.models import MasDatosUsuario
from .forms import MyUserCreationForm, MyUserEditForm
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('usuario')
            contraseña = form.cleaned_data.get('contraseña')
            
            usuario = authenticate(usuario=usuario, contraseña=contraseña)
            
            if usuario is not None:
                django_login(request, usuario)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'form': form})
        else:
            return render(request, 'accounts/login.html', {'form': form})
        
    
    form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'accounts/register.html', {'form': form})
        
    form = MyUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')

@login_required
def editar_perfil(request):
    
    user = request.user
    mas_datos_usuario, _ = MasDatosUsuario.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuario.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuario.avatar
                
            mas_datos_usuario.save()
            user.save()
            
            
            return redirect('perfil')
        else:
            return render(request, 'accounts/editar_perfil.html', {'form': form})
        
    form = MyUserEditForm(
            initial={
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'avatar': mas_datos_usuario.avatar
            }
    )
        
    return render(request, 'accounts/editar_perfil.html', {'form': form})

class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/cambio_password.html'
    success_url = '/accounts/perfil/'
