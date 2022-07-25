from django.shortcuts import render
from guilsportfolio.core.models import Profile, Project

"""
The system is designed so it renders only one profile.
It was preferable to select the profile by username instead of an arbitrary instance
"""


def home(request):
    portfolio_username = 'Guilherme Forton Viotti'

    profile = Profile.objects.filter(name=portfolio_username)
    projects = Project.objects.filter(project_executive__name=portfolio_username)

    context = {
        'profile': profile,
        'projects': projects,
    }

    return render(request, 'index.html', context)
