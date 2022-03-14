from cgitb import text
from datetime import timedelta

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from polls.models import Choice, Question


def create_question(question_text: str, days: int):
    """Creates a question with question_text given, its published date is the given number of days offset to now:
        days var is negative for questions published in the past.
        days var is Positive for question that have yet to be published.
    """
    time = timezone.now() + timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_question(self):
        """If not question exists, an appropiate message is displayed"""
        #hago una petición http de tipo get sobre la url de la vista index
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No hay encuestas disponibles')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    #def tests_future_questions(self):#el atributo auto_now_add=True en los modelos hace que la fecha siempre sea al momento de crearse
    #    """Questions with pub_date in the future aren't displayed on the index page"""
    #    create_question('Future question', days=20)
    #    response = self.client.get(reverse('polls:index'))
    #    self.assertContains(response, 'No hay encuestas disponibles')
    #    self.assertQuerysetEqual(response.context['latest_question_list'], [])
        
    def test_past_questions(self):
        """Questions with pub_date in the past are displayed on the index page"""
        question = create_question('Past question', days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_more_than_one_question_displayed_ordered_by_pub_date(self):
        """Index page may display multiple questions"""
        question1 = create_question('Question 1', days=0)
        question2 = create_question('Question 2', days=0)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1]
        )


class QuestionDetailViewTests(TestCase):
    
    def setUp(self):
        self.question = Question.objects.create(question_text='Question')
        self.question.choice_set.create(choice_text='Choice 1')
        self.question.choice_set.create(choice_text='Choice 2')
    
    def test_displays_question_text(self):
        url = reverse('polls:detail', args=(self.question.id,))
        response = self.client.get(url)
        self.assertContains(response, self.question.question_text)

    def test_displays_choices_of_a_question(self):
        choices = self.question.choice_set.all()
        url = reverse('polls:detail', args=(self.question.id,))
        response = self.client.get(url)
        self.assertContains(response, choices[0])
        self.assertContains(response, choices[1])


class ResultsViewTests(TestCase):

    def setUp(self):
        self.question = Question.objects.create(question_text='Question')
        self.question.choice_set.create(choice_text='Choice 1')

    def test_displays_question_text(self):
        url = reverse('polls:results', args=(self.question.id,))
        response = self.client.get(url)
        self.assertContains(response, self.question.question_text)

    def test_displays_choices_of_a_question_and_its_votes(self):
        choices = self.question.choice_set.all()
        url = reverse('polls:results', args=(self.question.id,))
        response = self.client.get(url)
        self.assertContains(response, choices[0])
        self.assertContains(response, 'vote')
