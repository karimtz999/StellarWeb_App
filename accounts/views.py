from django.shortcuts import render

def profile(request):
    return render(request, 'accounts/profile.html')  # Ensure you have this template
