from django.test import TestCase

from . import models


class PostModelTest(TestCase):

    def test_string_representation(self):
        post = models.Post(title="Test title")
        self.assertEqual(str(post), post.title)


class TagModelTest(TestCase):

    def test_string_representation(self):
        tag = models.Tag(name="Test tag")
        self.assertEqual(str(tag), tag.name)
