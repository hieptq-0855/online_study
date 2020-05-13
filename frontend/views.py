from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import *
from frontend.forms import LoginForm
from frontend.models import Category
from frontend import custom_backend
import django.contrib.auth as auth


@require_GET
def index(request):
    context = Category.objects.prefetch_related('exam_set')

    return render(request, 'frontend/index.html', {'context': context})


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = custom_backend.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)

                return redirect('index')
            else:
                return render(request, 'frontend/login.html', {'message_error': 'Email or password is incorrect!!'})
        else:
            return render(request, 'frontend/login.html', {'form': form})
    else:
        if request.user.is_authenticated:
            return redirect('index')

        return render(request, 'frontend/login.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
