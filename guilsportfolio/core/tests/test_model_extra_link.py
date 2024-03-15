from django.db import models
from .test_setup import CommonTestSetup
from guilsportfolio.core.models import ExtraLink


class LinkModelTest(CommonTestSetup):

    def test_create_link(self):
        """Test the link object is created"""
        self.assertTrue(ExtraLink.objects.exists())

    def test_url_display_field(self):
        """Test the url_display field configuration"""
        field = ExtraLink._meta.get_field('url_display')
        self.assertEqual(field.max_length, 255)

    def test_url_field(self):
        """Test the url field configuration"""
        field = ExtraLink._meta.get_field('url')
        self.assertTrue(isinstance(field, models.URLField))

    def test_link_position_field(self):
        """Test the position field configuration."""
        field = ExtraLink._meta.get_field('position')
        self.assertTrue(field.null)

    def test_update_link(self):
        """Test if an ExtraLink instance can be successfully updated."""
        new_url_display = "new website"
        self.link.url_display = new_url_display
        self.link.save()
        self.assertEqual(self.link.url_display, new_url_display)

    def test_link_extra_relationship(self):
        """Test if an ExtraLink instance is correctly related to Extra."""
        self.assertEqual(self.link.extra, self.extra)