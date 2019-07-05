from django.test import TestCase
from . import views

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response=self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response=self.client.get('/')
        self.assertContains(response,'<h1>homepage</h1>')
    
    def test_home_page_does_not_contain_incorrect_html(self):
        response=self.client.get('/')
        self.assertNotContains(response,'hi there')
    
    def test_view_users_correct_template(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'testpage.html')
