import datetime

from collections import OrderedDict
from django.test import TestCase
from .models import New
from django.utils import timezone


class BandTest(TestCase):

    def setUp(self):
        first_article, _ = New.objects.get_or_create(
            title='First Article',
            pub_date = timezone.now(),
            description=('This is the first article of the app ever'))
        second_article, _ = New.objects.get_or_create(
            title='Second Article',
            pub_date = timezone.now(),
            description=('This is the second article of the app, kind of boring'))

    def test_new_search(self):
        new_queryset = New.objects.search(
            'app').values_list('title', 'rank')
        new_objects = list(
            OrderedDict(new_queryset).items())
        new_list = [
            ('First Article', 0.243171),
            ('Second Article', 0.243171)]
        self.assertSequenceEqual(new_objects, new_list)