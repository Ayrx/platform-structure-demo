from django.test import TestCase
from django.urls import reverse

class TodoViewTests(TestCase):
    def test_index_view_status_code(self):
        """The index page should return a 200 OK status code."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        """The index page should render the todo_app/index.html template."""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'todo_app/index.html')
        self.assertContains(response, 'My To-Do List')

