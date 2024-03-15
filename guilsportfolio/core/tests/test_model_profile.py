from django.core.exceptions import ValidationError
from .test_setup import CommonTestSetup
from guilsportfolio.core.models import Profile, Expertise, Competency


class ProfileModelTest(CommonTestSetup):

    def test_create_profile(self):
        self.assertTrue(Profile.objects.exists())

    def test_cannot_create_more_than_one_profile(self):
        """Test that only one Profile can be created"""
        with self.assertRaises(ValidationError):
            Profile.objects.create(
                name="Test Profile 2",
                nickname="Test 2",
                picture="https://example.com/picture2.png",
                bio="Test bio 2",
                github_link="https://github.com/testuser2",
                linkedin_link="https://www.linkedin.com/in/testuser2/",
                email="test2@email.com",
            )

    def test_blank_fields(self):
        for field in self.profile_blank_fields:
            test_field = Profile._meta.get_field(field)
            self.assertTrue(test_field.blank)

    def test_null_fields(self):
        for field in self.profile_null_fields:
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


class ExpertiseModelTest(CommonTestSetup):
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


class CompetencyModelTest(CommonTestSetup):
    def setUp(self):
        self.competency = Competency.objects.create(
            competency='Software Developer',
            icon='https://www.dropbox.com/s/0epvqodt0bj51gl/pixel_me.png?raw=1',
            proficiency=1,
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

    def test_proficiency_choices(self):
        """Competency should be limited to 1, 2 or 3"""
        competency = Competency(competency=self.competency, proficiency=4)
        self.assertRaises(ValidationError, competency.full_clean)
