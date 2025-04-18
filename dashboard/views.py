from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')


def profile(request):
    return render(request, 'profile.html')
