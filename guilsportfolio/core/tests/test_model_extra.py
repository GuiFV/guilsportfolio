from .test_setup import CommonTestSetup
from guilsportfolio.core.models import Extra


class ExtraModelTest(CommonTestSetup):

    def test_create_extra(self):
        self.assertTrue(Extra.objects.exists())

    def test_extra_name_field(self):
        """ Check if name field has the correct configuration """
        field = Extra._meta.get_field('name')
        self.assertTrue(field.blank)
        self.assertTrue(field.null)

    def test_extra_type_field(self):
        """ Check if type defaults to AWARD """
        field = Extra._meta.get_field('type')
        # Check if 'type' field has correct choices set
        self.assertEqual(field.choices, Extra.TYPE)
        # Check if 'type' field defaults to AWARD
        self.assertEqual(self.extra.type, Extra.AWARD)

    def test_extra_multiple_links(self):
        """ Check if Extra instance can have multiple links """
        extra_links = self.extra.extralink_set.all()

        self.assertEqual(len(extra_links), 2)  # it should find 2 links associated with 'extra' instance
        self.assertIn(self.link, extra_links)  # it should find 'link' in the links associated with 'extra'
        self.assertIn(self.link2, extra_links)  # it should find 'link2' in the links associated with 'extra'

    def test_extra_image_field(self):
        """ Check if extra image field has the correct configuration """
        field = Extra._meta.get_field('image')
        self.assertTrue(field.blank)
        self.assertTrue(field.null)
        self.assertEqual(self.extra.image, 'https://example.com/image.png')

    def test_extra_description_field(self):
        """ Check if extra description field has the correct configuration """
        field = Extra._meta.get_field('description')
        self.assertTrue(field.blank)
        self.assertTrue(field.null)
        self.assertEqual(self.extra.description, 'Test Description')

    def test_extra_position_field(self):
        """ Check if extra position field has the correct configuration """
        field = Extra._meta.get_field('position')
        self.assertTrue(field.null)
        self.assertEqual(self.extra.position, 1)

    def test_update_extra(self):
        """ Check if update extra instance is valid """
        new_name = "New Test Name"
        self.extra.name = new_name
        self.extra.save()
        self.assertEqual(self.extra.name, new_name)

    def test_extra_profile_relationship(self):
        """ Check if extra profile relationship is valid """
        self.assertEqual(self.extra.profile, self.profile)

    def test_extra_string_representation(self):
        """ Check if extra returns the correct string representation """
        self.assertEqual(str(self.extra), self.extra.name)
