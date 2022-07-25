from django.core.exceptions import ValidationError
from django.test import TestCase
from guilsportfolio.core.models import Project, Technologies, Profile


class ProjectModelTest(TestCase):
    def setUp(self):
        self.blank_fields = (
            'project_executive',
            'project_technologies',
            'project_image',
            'project_description',
            'project_link',
            'project_button_description',
        )

        self.null_fields = (
            'project_executive',
            'project_title',
            'project_subtitle',
            'project_image',
            'project_description',
            'project_link',
            'project_button_description',
            'project_position',
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
            project_executive=self.profile,
            project_title='Project 1',
            project_subtitle='Some short description here',
            project_image='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1',
            project_category='Software Development',
            project_description='Big text field here',
            project_link='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1',
            project_button_description='Check out this project',
            project_position='1',
            show_or_hide='True',
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
        self.project.project_technologies.create(
            technology='Python'
        )
        self.assertEqual(1, self.project.project_technologies.count())

    def test_category(self):
        Project.objects.create(project_executive=self.profile,
                               project_category=Project.PROJECT_CATEGORY,
                               )

        self.assertTrue(Project.objects.exists())

    def test_choices(self):
        """ Project category should be limited to it's choices """
        project = Project.objects.create(project_executive=self.profile,
                                         project_category="A",
                                         )
        self.assertRaises(ValidationError, project.full_clean)

# Technologies tests


class TechnologiesModelTest(TestCase):
    def setUp(self):
        self.technologies = Technologies.objects.create(
            technology='Python'
        )

    def test_create_expertise(self):
        self.assertTrue(Technologies.objects.exists())

    def test_expertise_null(self):
        field = Technologies._meta.get_field('technology')
        self.assertTrue(field.null)
