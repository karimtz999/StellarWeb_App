from django.shortcuts import render

def api_home(request):
    return render(request, 'api/home.html')  # Ensure you have this template
