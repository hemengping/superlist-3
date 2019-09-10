from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/home/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        print(f"html:{html}")
        self.assertTrue(html.startswith('H'))
        self.assertIn('<title>To-Do lists</tittle>',html)
        self.assertTrue(html.endswith('d'))

