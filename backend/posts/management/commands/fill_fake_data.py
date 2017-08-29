from random import choice, randint

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

from backend.posts import models


class Command(BaseCommand):
    help = 'Create fake posts for dev server'

    def handle(self, *args, **options):
        User = get_user_model()
        fake = Faker()

        admin = User.objects.create_user(
            username='admin',
            password='password13',
            is_staff=True,
            is_superuser=True,
        )

        tag_names = set()
        for _ in range(15):
            tag_names.add(fake.word())

        tag_ids = []
        for name in tag_names:
            tag = models.Tag(name=name)
            tag.save()
            tag_ids.append(tag.id)

        for _ in range(100):
            post = models.Post(
                author=admin,
                title=fake.sentence(nb_words=randint(3, 8)),
                text='\n'.join(fake.paragraphs(nb=randint(10, 30))),
                hidden=choice([True, False, False]),
            )
            post.save()

            tags = set()
            for _ in range(randint(3, 8)):
                tags.add(choice(tag_ids))

            for tag in tags:
                post.tags.add(tag)
            post.save()

        self.stdout.write(self.style.SUCCESS('Done'))
