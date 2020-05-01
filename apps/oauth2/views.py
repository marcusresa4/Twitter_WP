from django.contrib.messages.storage import session
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html', {})
