from django.core.exceptions import ValidationError
from django.test import TestCase
from guilsportfolio.core.models import Project, Technologies, Profile, Expertise


class ProjectModelTest(TestCase):
    def setUp(self):
        self.blank_fields = (
            'executive',
            'technologies',
            'image',
            'description',
            'link',
            'button_description',
        )

        self.null_fields = (
            'executive',
            'title',
            'subtitle',
            'image',
            'description',
            'link',
            'button_description',
            'position',
        )

        self.profile = Profile.objects.create(
            name="Guilherme Forton Viotti",
            nickname="Guil",
            picture="https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1",
            bio="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            github_link="https://github.com/GuiFV",
            linkedin_link="https://www.linkedin.com/in/guilhermeviotti/",
            email="some@email.com",
        )
        self.project = Project.objects.create(
            executive=self.profile,
            title='Project 1',
            subtitle='Some short description here',
            image='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1',
            description='Big text field here',
            link='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1',
            button_description='Check out this project',
            position='1',
            show='True',
        )

    def test_create_profile(self):
        self.assertTrue(Project.objects.exists())

    def test_blank_fields(self):
        for field in self.blank_fields:
            test_field = Project._meta.get_field(field)
            self.assertTrue(test_field.blank)

    def test_null_fields(self):
        for field in self.null_fields:
            test_field = Project._meta.get_field(field)
            self.assertTrue(test_field.null)

    def test_has_technologies(self):
        """ Project has many technologies and vice-versa"""
        self.project.technologies.create(
            technology='Python'
        )
        self.assertEqual(1, self.project.technologies.count())

    def test_has_areas_of_expertise(self):
        """ Project has many areas of expertise and vice-versa"""
        self.project.areas_of_expertise.create(
            expertise='Software Developer'
        )
        self.assertEqual(1, self.project.areas_of_expertise.count())


# Technologies tests


class TechnologiesModelTest(TestCase):
    def setUp(self):
        self.technologies = Technologies.objects.create(
            technology='Python'
        )

    def test_create_technologies(self):
        self.assertTrue(Technologies.objects.exists())

    def test_technologies_null(self):
        field = Technologies._meta.get_field('technology')
        self.assertTrue(field.null)

# Technologies tests


class AreasOfExpertiseModelTest(TestCase):
    def setUp(self):
        self.expertise = Expertise.objects.create(
            expertise='Software Developer'
        )

    def test_create_expertise(self):
        self.assertTrue(Expertise.objects.exists())

    def test_expertise_null(self):
        field = Expertise._meta.get_field('expertise')
        self.assertTrue(field.null)
