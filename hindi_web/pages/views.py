from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, 'login.html')


def introduction(request):
    return render(request, 'introduction-main.html')


def community(request):
    return render(request, 'community-main.html')
