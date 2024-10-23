from django.shortcuts import render
from django.utils.text import slugify
from django.db.models import Case, When

from guilsportfolio.core.models import Profile, Project, Extra, Expertise


def home(request):

    profile = Profile.objects.first()  # Only one Profile is allowed in the DB
    projects = Project.objects.filter(executive__name=profile.name)
    expertises = Expertise.objects.filter(profile=profile).order_by(
        Case(  # Implemented to manipulate the order of top menu
            When(id=2, then=0),  # First, Software Developer
            When(id=1, then=1),  # Then, Project Manager
            default=2,  # Finally, the rest
        ),
        'expertise'
    )

    display = None  # For filtering expertises and manipulating button's logic
    extras = Extra.objects.all()

    if request.GET.get('expertise'):
        expertise = request.GET['expertise']
        display = slugify(expertise)
        projects = projects.filter(areas_of_expertise__expertise__icontains=expertise)

    context = {
        'profile': profile, 'projects': projects, 'display': display, 'extras': extras, 'expertises': expertises,
    }

    return render(request, 'index.html', context)
