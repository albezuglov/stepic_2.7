from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *

# Create your views here.
def signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = SignupForm()

    return render(request, 'signup_form.html', {'form': form})


def mylogin(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data['username'], form.cleaned_data['password'])
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "Invalid login data")
    else:
        form = LoginForm()

    return render(request, 'login_form.html', {'form': form})
