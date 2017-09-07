
import factory


class BaseFactory(factory.django.DjangoModelFactory):
    id = factory.Sequence(lambda n: n)


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'

    username = factory.Faker('user_name')
    password = factory.Faker('password')


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'posts.Tag'

    name = factory.Faker('word')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'posts.Post'

    author = factory.SubFactory(AuthorFactory)
    title = factory.Faker('sentence')
    text = factory.Faker('text')
    tags = factory.RelatedFactory(TagFactory)
    hidden = False
