import factory
from factory.django import DjangoModelFactory

from users.tests.factories import UserFactory


class PostFactory(DjangoModelFactory):
    title = factory.faker.Faker("bothify", text="My article ???????????")
    text = factory.faker.Faker("text")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = 'posts.Post'


class LikeFactory(DjangoModelFactory):

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

    class Meta:
        model = 'posts.Like'
