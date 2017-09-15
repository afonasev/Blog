from random import choice, randint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from backend.posts import models

fake = Faker()


def make_text(min_paragraphs, max_paragraphs):
    return '\n'.join(fake.paragraphs(
        nb=randint(min_paragraphs, max_paragraphs)
    ))


class Command(BaseCommand):
    help = 'Fill fake data for dev server'

    def handle(self, *args, **options):
        admin = self._create_admin_user()
        tag_ids = self._create_tags()
        posts = self._create_posts(author=admin, tags=tag_ids)
        self._create_comments(author=admin, posts=posts)
        self.stdout.write(self.style.SUCCESS('Fake data filled!'))

    @staticmethod
    def _create_admin_user():
        return get_user_model().objects.create_user(
            username='admin',
            password='password13',
            is_staff=True,
            is_superuser=True,
        )

    def _create_tags(self):
        tag_names = set()
        for _ in range(15):
            tag_names.add(fake.word())

        tag_ids = []
        for name in tag_names:
            tag = models.Tag(title=name)
            tag.save()
            tag_ids.append(tag.id)

        return tag_ids

    def _create_posts(self, author, tags):
        posts = []
        for _ in range(100):
            post = models.Post(
                author=author,
                title=fake.sentence(nb_words=randint(3, 8)),
                text=make_text(10, 30),
                hidden=choice([True, False, False]),
            )
            post.save()

            post_tags = set()
            for _ in range(randint(3, 8)):
                post_tags.add(choice(tags))

            for tag in post_tags:
                post.tags.add(tag)
            post.save()

            posts.append(post)

        return posts

    def _create_comments(self, author, posts):
        for post in posts:
            for _ in range(randint(5, 20)):
                has_author = randint(1, 5) < 2
                models.Comment(
                    post=post,
                    author=author if has_author else None,
                    username=fake.user_name() if not has_author else None,
                    text=make_text(1, 3),
                ).save()
