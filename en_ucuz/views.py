from django.shortcuts import render

def en_ucuz(request):
    return render(request, 'en_ucuz/main.html')
