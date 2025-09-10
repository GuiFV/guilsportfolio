from django.core.exceptions import ValidationError
from django.db import models


class Profile(models.Model):
    """ Access all data through Profile """
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

    def save(self, *args, **kwargs):
        """Singleton-like pattern:
        Prevents creation of more than one Profile
        Checks if PK exists so current Profile can be updated"""
        if not self.pk and Profile.objects.exists():
            raise ValidationError('You can only have one Profile')
        return super(Profile, self).save(*args, **kwargs)


class Expertise(models.Model):
    """ Associated with Profile and Projects (for filtering) """
    expertise = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = 'expertise'
        verbose_name_plural = 'expertise'

    def __str__(self):
        return self.expertise

    # Uncomment below to constrain expertises

    # def save(self, *args, **kwargs):
    #     """Limit expertises (up to 3)"""
    #     if Expertise.objects.all().count() < 3:
    #         return super(Expertise, self).save(*args, **kwargs)
    #
    #     raise ValidationError("Not a good practice to have more than 3 Expertises")


class Competency(models.Model):
    """ Associated with Profile """

    ONE = 1
    TWO = 2
    THREE = 3

    PROFICIENCY = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
    )

    competency = models.CharField(max_length=20, null=True)
    icon = models.URLField(null=True, blank=True)
    proficiency = models.PositiveSmallIntegerField(choices=PROFICIENCY, default=1)

    class Meta:
        verbose_name = 'competency'
        verbose_name_plural = 'competencies'

    def __str__(self):
        return self.competency


class Project(models.Model):
    """ Associated with Profile """
    executive = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    technologies = models.ManyToManyField('Technologies', blank=True)
    image = models.URLField(null=True, blank=True)
    areas_of_expertise = models.ManyToManyField('Expertise', blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    button_description = models.CharField(max_length=50, null=True, blank=True)
    position = models.IntegerField(null=True)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Technologies(models.Model):
    """ Associated with Project """
    technology = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = 'technology'
        verbose_name_plural = 'technologies'

    def __str__(self):
        return self.technology


class ExtraLink(models.Model):
    extra = models.ForeignKey('Extra', null=True, blank=True, on_delete=models.CASCADE)
    url_display = models.CharField(max_length=255)
    url = models.URLField()
    position = models.IntegerField(null=True)

    def __str__(self):
        return self.url_display


class Extra(models.Model):
    """ Associated with Profile """

    AWARD = 'aw'
    TALK = 'ta'
    CERTIFICATION = 'ce'
    PAPER = 'pa'

    TYPE = (
        (AWARD, 'award'),
        (TALK, 'talk'),
        (CERTIFICATION, 'certification'),
        (PAPER, 'paper'),
    )

    profile = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE, default=AWARD)
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    position = models.IntegerField(null=True)

    def __str__(self):
        return self.name
