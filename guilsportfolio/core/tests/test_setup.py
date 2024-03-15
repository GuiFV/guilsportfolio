from django.test import TestCase
from guilsportfolio.core.models import Extra, Profile, Project, ExtraLink


class CommonTestSetup(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.project_blank_fields = (
            'executive',
            'technologies',
            'image',
            'description',
            'link',
            'button_description',
        )

        cls.project_null_fields = (
            'executive',
            'title',
            'subtitle',
            'image',
            'description',
            'link',
            'button_description',
            'position',
        )

        cls.profile_blank_fields = (
            'areas_of_expertise',
            'picture',
            'bio',
            'competencies',
            'github_link',
            'linkedin_link',
            'email',
        )

        cls.profile_null_fields = (
            'name',
            'nickname',
            'picture',
            'bio',
            'github_link',
            'linkedin_link',
            'email',
        )

        cls.profile = Profile.objects.create(
            name="Guilherme Forton Viotti",
            nickname="Guil",
            picture="https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1",
            bio="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            github_link="https://github.com/GuiFV",
            linkedin_link="https://www.linkedin.com/in/guilhermeviotti/",
            email="some@email.com",
        )

        cls.extra = Extra.objects.create(
            profile=cls.profile,
            type=Extra.AWARD,
            name='Test Award',
            image='https://example.com/image.png',
            description='Test Description',
            position=1,
        )

        cls.link = ExtraLink.objects.create(
            extra=cls.extra,
            url_display="website 1",
            url="https://example.com",
            position=1
        )

        cls.link2 = ExtraLink.objects.create(
            extra=cls.extra,
            url_display="website 2",
            url="https://example2",
            position=2
        )

        cls.project = Project.objects.create(
            executive=cls.profile,
            title='Project 1',
            subtitle='Some short description here',
            image='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1',
            description='Big text field here',
            link='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1',
            button_description='Check out this project',
            position='1',
            show='True',
        )
