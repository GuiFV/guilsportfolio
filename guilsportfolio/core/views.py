from django.shortcuts import render
from django.utils.text import slugify

from guilsportfolio.core.models import Profile, Project


def home(request):

    profile = Profile.objects.first()  # Only the first Profile inserted in the database renders
    projects = Project.objects.filter(project_executive__name=profile.name)
    display = None  # For filtering expertises and manipulating button's logic

    if request.GET.get('expertise'):
        expertise = request.GET['expertise']
        display = slugify(expertise)
        projects = projects.filter(areas_of_expertise__expertise__icontains=expertise)

    context = {
        'profile': profile,
        'projects': projects,
        'display': display,
    }

    return render(request, 'index.html', context)
