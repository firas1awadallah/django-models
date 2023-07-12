from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class TestHome(TestCase):
    def test_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)


    def test_home_page_templates(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        
        
        
    def test_status_snacks_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
       
        self.assertEqual(response.status_code, 200)


    def test_snacks_list_page_templates(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks_list.html')  
        
              
 