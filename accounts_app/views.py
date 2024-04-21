from django.shortcuts import render

def login(request):
    return render(request, 'accounts_app/login.html', context={})