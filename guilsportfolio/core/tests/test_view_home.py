from django.test import TestCase
from django.shortcuts import resolve_url as r
from guilsportfolio.core.models import Profile


class HomeTest(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name="Guilherme Viotti")
        self.response = self.client.get(r('home'))
        self.response_with_query = self.client.get(r('home'), {'expertise': 'Project+Manager'})
        self.response_with_blank_query = self.client.get(r('home'), {'expertise': ''})

    def test_get(self):
        """ GET / must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use index.html """
        self.assertTemplateUsed(self.response, 'index.html')

    def test_get_with_query(self):
        """ GET /expertise must return status code 200 """
        self.assertEqual(200, self.response_with_query.status_code)

    def test_template_with_query(self):
        """ Must use index.html with get query"""
        self.assertTemplateUsed(self.response_with_query, 'index.html')

    def test_get_with_blank_query(self):
        """ GET /expertise=None must return status code 200 """
        self.assertEqual(200, self.response_with_blank_query.status_code)

    def test_template_with_blank_query(self):
        """ Must use index.html with empty get query"""
        self.assertTemplateUsed(self.response_with_blank_query, 'index.html')
