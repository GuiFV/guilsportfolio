from .test_setup import CommonTestSetup
from guilsportfolio.core.models import Project, Technologies, Expertise


class ProjectModelTest(CommonTestSetup):

    def test_create_profile(self):
        self.assertTrue(Project.objects.exists())

    def test_blank_fields(self):
        for field in self.project_blank_fields:
            test_field = Project._meta.get_field(field)
            self.assertTrue(test_field.blank)

    def test_null_fields(self):
        for field in self.project_null_fields:
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


class TechnologiesModelTest(CommonTestSetup):
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


class AreasOfExpertiseModelTest(CommonTestSetup):
    def setUp(self):
        self.expertise = Expertise.objects.create(
            expertise='Software Developer'
        )

    def test_create_expertise(self):
        self.assertTrue(Expertise.objects.exists())

    def test_expertise_null(self):
        field = Expertise._meta.get_field('expertise')
        self.assertTrue(field.null)
