from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog/home.html')  # Ensure you have this template
