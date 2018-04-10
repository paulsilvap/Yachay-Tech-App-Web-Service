from django.test import TestCase
from  django.utils  import  unittest
#importo clase de models.py
from .models import New
import datetime

from django.utils import timezone

class New(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    def __str__(self):
        return self.description
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        ordering = ('pub_date',)

#test

#tamaño maximo de title and descrption
class MaxLengthArgumentsTests(unittest.TestCase):
    def verify_max_length(self, model, field, length):
        self.assertEqual(model._meta.get_field(field).max_length, length)

    def test__max_lengths(self):
        self.verify_max_length(New, 'title', 200)
        self.verify_max_length(New, 'description', 200)

class MaxLengthTest(unittest.TestCase):
    def _max_lengths(self):
        args = {
            "title": "A dynamic way of implementation",
            "description": "This talk is about the knowledge.................."
        }

        for field in ("title", "description"):
            new_args = args.copy()
            new_args[field] = "X" * 200  # a value longer than any of the default fields could hold.
            p = New.objects.create(**new_args)
            self.assertEqual(getattr(p, field), ("X" * 200))


class QuestionModelTests(unittest.TestCase):

    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        question = New(pub_date=time)
        self.assertIs(question.was_published_recently(), False)
