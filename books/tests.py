"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime

from django.utils import timezone
from django.test import TestCase

from books.models import Post


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class PostMethodTests(TestCase):

    def test_was_posted_recently_with_future_poll(self):
        """
        was_posted_recently() should return False for post whose
        pub_date is in the future
        """
        future_post = Post(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_post.was_posted_recently(), False)