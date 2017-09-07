from django.test import TestCase
from django.urls import reverse

from . import factories, models


class PostModelTest(TestCase):

    def test_string_representation(self):
        post = factories.PostFactory()
        self.assertEqual(str(post), post.title)

    def test_html(self):
        post = factories.PostFactory()
        self.assertEqual(post.html, f'<p>{post.text}</p>\n')

    def test_unhidden(self):
        hidden_post = factories.PostFactory(hidden=True)
        visible_post = factories.PostFactory(hidden=False)
        posts = models.Post.unhidden()
        assert visible_post in posts
        assert hidden_post not in posts

    def test_get_absolute_url(self):
        post = factories.PostFactory(slug='test')
        formated_date = post.created_at.strftime('%Y/%m/%d')
        assert post.get_absolute_url() == '/%s/test/' % formated_date


class TagModelTest(TestCase):

    def test_string_representation(self):
        tag = factories.TagFactory()
        self.assertEqual(str(tag), tag.title)

    def test_get_absolute_url(self):
        tag = factories.TagFactory(slug='test')
        assert tag.get_absolute_url() == '/tag/test/'


class PostListViewTest(TestCase):

    def test_list(self):
        posts = factories.PostFactory.create_batch(3)
        response = self.client.get('/')
        for post in posts:
            assert post.title in response.content.decode()

    def test_hidden(self):
        visible_post = factories.PostFactory(hidden=False)
        hidden_post = factories.PostFactory(hidden=True)
        response = self.client.get(reverse('posts:post-list'))
        assert visible_post.title in response.content.decode()
        assert hidden_post.title not in response.content.decode()


class PostDetailViewTest(TestCase):

    def test_detail(self):
        post = factories.PostFactory()
        response = self.client.get(post.get_absolute_url())
        assert post.title in response.content.decode()

    def test_tag(self):
        post = factories.PostFactory()
        tag = factories.TagFactory()
        post.tags.add(tag)
        response = self.client.get(post.get_absolute_url())
        assert tag.title in response.content.decode()

    def test_404(self):
        url = reverse('posts:post-detail', kwargs={
            'year': '2017', 'month': '01', 'day': '01', 'slug': 'slug',
        })
        response = self.client.get(url)
        assert response.status_code == 404


class PostByTagListViewTest(TestCase):

    def test_list(self):
        tag = factories.TagFactory(title='test')
        post_without_tag = factories.PostFactory()
        post_with_tag = factories.PostFactory()
        post_with_tag.tags.add(tag)
        response = self.client.get(tag.get_absolute_url())
        assert post_with_tag.title in response.content.decode()
        assert post_without_tag.title not in response.content.decode()
