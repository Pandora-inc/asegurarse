from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import CreateUserForm


def registerPage(request):
    # if request.user.is_authenticated:
        return redirect('inicio')
    # else:
    #     form = CreateUserForm()
    #     if request.method == 'POST':
    #         form = UserCreationForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             user = form.cleaned_data.get('username')
    #             messages.success(request, 'Account was created for ' + user)
    #
    #             return redirect('login')
    #
    #     context = {'form': form}
    #     return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def inicio(request):
    return render(request, "panel.html", {'navbar': 'actividad'})
