import unittest
import json
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        """Test the main endpoint"""
        response = self.app.get('/')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Hello World!')
        self.assertIn('timestamp', data)
        self.assertIn('version', data)

    def test_health_check(self):
        """Test the health check endpoint"""
        response = self.app.get('/health')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', data)
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('timestamp', data)

    def test_app_info(self):
        """Test the app info endpoint"""
        response = self.app.get('/info')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('app_name', data)
        self.assertEqual(data['app_name'], 'CI/CD Demo App')
        self.assertIn('description', data)
        self.assertIn('environment', data)
        self.assertIn('version', data)

    def test_html_page(self):
        """Test the HTML page endpoint"""
        response = self.app.get('/html')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CI/CD Demo Application', response.data)
        self.assertIn(b'Successfully Deployed', response.data)

    def test_404_error(self):
        """Test 404 error handling"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
