from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('usuario')
            contraseña = form.cleaned_data.get('contraseña')
            
            usuario = authenticate(usuario=usuario, contraseña=contraseña)
            
            if usuario is not None:
                django_login(request, usuario)
                return redirect('index.html')
            else:
                return render(request, 'accounts/login.html', {'form': form})
        else:
            return render(request, 'accounts/login.html', {'form': form})
        
    
    form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})
