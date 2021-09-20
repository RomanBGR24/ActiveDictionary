from django.test import TestCase

# Create your tests here.
class Main_app(TestCase):
    def test_index_page_returns_correct_html(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'main_app/index.html')