from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

from polls.models import Question


class QuestionTests(TestCase):

    def setUp(self):
        self.question = Question.objects.create(question_text='Question')
        #self.question.choice_set.create(choice_text='Choice 1')

    def test_was_created_recently_with_future_questions(self):
        time = timezone.now() + timedelta(days=30)
        self.question.pub_date = time
        self.assertIs(self.question.was_created_recently(), False)
    
    def test_was_created_recently_with_present_questions(self):
        time = timezone.now() - timedelta(hours=23)
        self.question.pub_date = time
        self.assertIs(self.question.was_created_recently(), True)
    
    def test_was_created_recently_with_past_questions(self):
        time = timezone.now() - timedelta(days=1, minutes=1)
        self.question.pub_date = time
        self.assertIs(self.question.was_created_recently(), False)

    def test_question_created_with_no_choices(self):
        with self.assertRaises(ValidationError):
            self.question.clean()
