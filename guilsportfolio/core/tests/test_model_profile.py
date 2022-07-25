from django.test import TestCase
from guilsportfolio.core.models import Profile, Expertise, Competency


class ProfileModelTest(TestCase):
    def setUp(self):
        self.blank_fields = (
            'areas_of_expertise',
            'picture',
            'bio',
            'competencies',
            'github_link',
            'linkedin_link',
            'email',
        )

        self.null_fields = (
            'name',
            'nickname',
            'picture',
            'bio',
            'github_link',
            'linkedin_link',
            'email',
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

    def test_create_profile(self):
        self.assertTrue(Profile.objects.exists())

    def test_blank_fields(self):
        for field in self.blank_fields:
            test_field = Profile._meta.get_field(field)
            self.assertTrue(test_field.blank)

    def test_null_fields(self):
        for field in self.null_fields:
            test_field = Profile._meta.get_field(field)
            self.assertTrue(test_field.null)

    def test_has_areas_of_expertise(self):
        """ Profile has many areas of expertise and vice-versa """
        self.profile.areas_of_expertise.create(
            expertise='Software Developer'
        )
        self.assertEqual(1, self.profile.areas_of_expertise.count())

    def test_has_competencies(self):
        """ Profile has many competencies and vice-versa """
        self.profile.competencies.create(
            competency='Django',
            icon='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1'
        )
        self.assertEqual(1, self.profile.competencies.count())

# Expertise tests


class ExpertiseModelTest(TestCase):
    def setUp(self):
        self.expertise = Expertise.objects.create(
            expertise='Software Developer'
        )

    def test_create_expertise(self):
        self.assertTrue(Expertise.objects.exists())

    def test_expertise_null(self):
        field = Expertise._meta.get_field('expertise')
        self.assertTrue(field.null)

# Competency tests


class CompetencyModelTest(TestCase):
    def setUp(self):
        self.competency = Competency.objects.create(
            competency='Software Developer',
            icon='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1',
        )

    def test_create_competency(self):
        self.assertTrue(Competency.objects.exists())

    def test_competency_blank(self):
        field = Competency._meta.get_field('icon')
        self.assertTrue(field.blank)

    def test_competency_null(self):
        field1 = Competency._meta.get_field('competency')
        field2 = Competency._meta.get_field('icon')
        self.assertTrue(field1.null)
        self.assertTrue(field2.null)

