from django.test import TestCase, Client
from django.urls import reverse
from .models import Link

# Create your tests here.

class LinkModelTest(TestCase):
    def test_create_link(self):
        link = Link.objects.create(original_url='https://www.example.com')
        self.assertEqual(link.original_url, 'https://www.example.com')
        self.assertTrue(link.short_code)
        self.assertEqual(len(link.short_code), 6)

    def test_unique_short_code(self):
        link1 = Link.objects.create(original_url='https://www.example1.com')
        link2 = Link.objects.create(original_url='https://www.example2.com')
        self.assertNotEqual(link1.short_code, link2.short_code)

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_index_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/index.html')

    def test_index_post_valid_url(self):
        response = self.client.post(self.url, {'url': 'https://www.example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/index.html')
        self.assertContains(response, 'URL encurtada:')

    def test_index_post_invalid_url(self):
        response = self.client.post(self.url, {'url': 'invalid-url'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/index.html')
        self.assertContains(response, 'URL inválida')

    def test_redirect_to_url(self):
        link = Link.objects.create(original_url='https://www.example.com')
        response = self.client.get(reverse('redirect', args=[link.short_code]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'https://www.example.com')
