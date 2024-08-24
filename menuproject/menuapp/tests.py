from django.test import TestCase, Client
from .models import Question, Choice
import datetime
from django.urls import reverse


class QuestionTests(TestCase):
    def test_Question_text(self):
        question = Question.objects.create(
            question_text='what do you like most?',
            pub_date=datetime.datetime.now()
        )
        self.assertTrue(question.question_text == 'what do you like most?')


class ChoiceTests(TestCase):
    def test_Choice_question(self):
        choice = Choice.objects.create(
            question = Question.objects.create(
                question_text='what do you like most?',
                pub_date=datetime.datetime.now()
            ),
            choice_text='milk',
            votes=4
        )
        self.assertTrue(str(choice.question) == 'what do you like most?')

    def test_Question_text(self):
        choice = Choice.objects.create(
            question=Question.objects.create(
                question_text='what do you like most?',
                pub_date=datetime.datetime.now()
            ),
            choice_text='water',
            votes=4
        )
        self.assertTrue(choice.choice_text == 'water')

    def test_Question_votes(self):
        choice = Choice.objects.create(
            question=Question.objects.create(
                question_text='what do you like most?',
                pub_date=datetime.datetime.now()
            ),
            choice_text='water',
            votes=5
        )
        self.assertTrue(choice.votes == 5)


class ViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_GET(self):
        # mock the response
        response = self.client.get('')
        self.assertEqual(response.status_code,200)

    def test_index_GET(self):
        # mock the response
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'polls/index.html')

    def test_detail_WithIncorrectQuestionId(self):
        # mock the response
        response = self.client.get('-1')
        self.assertEqual(response.status_code, 404)





