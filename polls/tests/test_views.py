from django.test import TestCase
from django.urls.base import reverse


class QuestionIndexViewTests(TestCase):

    def tests_no_question(self):
        """If not question exists, an appropiate message is displayed"""
        #hago una petición http de tipo get sobre la url de la vista index
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No hay encuestas disponibles')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
