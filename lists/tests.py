from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.

class HomePageTest(TestCase):
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/home/')
    #     self.assertEqual(found.func,home_page)

    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf-8')
    #     print(f"html:{html}")
    #     self.assertTrue(html.startswith('<!DOCTYPE html>'))
    #     self.assertIn('<title>To-Do lists</title>',html)
    #     self.assertTrue(html.endswith('d'))

    # def test_home_page_returns_correct_html(self):
    #     response = self.client.get('/home/')
    #     html = response.content.decode('utf-8')
    #     self.assertTrue(html.startswith('<!DOCTYPE html>'))
    #     self.assertTemplateUsed(response,'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/home/')
        self.assertTemplateUsed(response,'home.html')




