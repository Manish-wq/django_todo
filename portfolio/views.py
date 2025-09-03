from django.shortcuts import render
from .models import Project

def portfolio_home(request):
    """
    This view renders the main portfolio page.
    """
    # Fetch all projects from the database, ordered by 'display_order'
    projects = Project.objects.all()

    context = {
        'name': 'Manish Singh', # Replace with your name
        'tagline': 'Full-Stack Developer | Python | Django | Node | React | React Native',
        'projects': projects
    }
    return render(request, 'portfolio_home.html', context)