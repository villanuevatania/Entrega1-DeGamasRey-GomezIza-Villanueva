from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
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
    
    if request.method == 'POST':
        form = MyUserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            
            user.email = data.get('email') if data.get('email') else user.email
                
            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password(data.get('password1'))
            user.save()
            
            
            return redirect('perfil')
        else:
            return render(request, 'accounts/editar_perfil.html', {'form': form})
        
    form = MyUserEditForm(
            initial={
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name
            }
    )
        
    return render(request, 'accounts/editar_perfil.html', {'form': form})
