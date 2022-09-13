from django.shortcuts import render
from guilsportfolio.core.models import Profile, Project

"""
The system is designed to render only one profile (the first on Database)
"""


def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.filter(project_executive__name=profile.name)

    context = {
        'profile': profile,
        'projects': projects,
    }

    return render(request, 'index.html', context)
