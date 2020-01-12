from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from edu.views import home_page

class HomepageTest(TestCase):

    def test_root_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)