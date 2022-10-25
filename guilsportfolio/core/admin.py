from django.contrib import admin

from guilsportfolio.core.models import Profile, Expertise, Competency, Project, Technologies


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['position', 'title']


admin.site.register(Profile)
admin.site.register(Expertise)
admin.site.register(Competency)
admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Technologies)
