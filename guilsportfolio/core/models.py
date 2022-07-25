from django.db import models

"""
One profile holds many areas of expertise, many competencies and many projects.
One project holds one category and many involved technologies.
This way you can select one profile and access all necessary data.
"""


class Profile(models.Model):
    name = models.CharField(max_length=50, null=True)
    nickname = models.CharField(max_length=20, null=True)
    areas_of_expertise = models.ManyToManyField('Expertise', blank=True)
    picture = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    competencies = models.ManyToManyField('Competency', blank=True)
    github_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Expertise(models.Model):
    """ Associated with Profile """
    expertise = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = 'expertise'
        verbose_name_plural = 'expertise'

    def __str__(self):
        return self.expertise


class Competency(models.Model):
    """ Associated with Profile """
    competency = models.CharField(max_length=20, null=True)
    icon = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'competency'
        verbose_name_plural = 'competencies'

    def __str__(self):
        return self.competency


class Project(models.Model):
    """ Associated with Profile """
    PROJECT_MANAGEMENT = 'PM'
    SOFTWARE_DEVELOPMENT = 'SD'
    ENTREPRENEURSHIP = 'EN'
    SUSTAINABILITY = 'SU'

    PROJECT_CATEGORY = (
        (PROJECT_MANAGEMENT, 'Project Manager'),
        (SOFTWARE_DEVELOPMENT, 'Software Development'),
        (ENTREPRENEURSHIP, 'Entrepreneurship'),
        (SUSTAINABILITY, 'Sustainability'),
    )

    project_executive = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=30, null=True)
    project_subtitle = models.CharField(max_length=100, null=True)
    project_technologies = models.ManyToManyField('Technologies', blank=True)
    project_image = models.URLField(null=True, blank=True)
    project_category = models.CharField(max_length=2, choices=PROJECT_CATEGORY)
    project_description = models.TextField(null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)
    project_button_description = models.CharField(max_length=50, null=True, blank=True)
    project_position = models.IntegerField(null=True)
    show_or_hide = models.BooleanField(default=False)

    def __str__(self):
        return self.project_title


class Technologies(models.Model):
    """ Associated with Project """
    technology = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = 'technology'
        verbose_name_plural = 'technologies'

    def __str__(self):
        return self.technology
