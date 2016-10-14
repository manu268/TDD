from django.test import TestCase
from lists import views 
from django.core.urlresolvers import resolve

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, views.home_page)  