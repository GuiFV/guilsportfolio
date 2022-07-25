from django.contrib import admin

from guilsportfolio.core.models import Profile, Expertise, Competency, Project, Technologies

admin.site.register(Profile)
admin.site.register(Expertise)
admin.site.register(Competency)
admin.site.register(Project)
admin.site.register(Technologies)
