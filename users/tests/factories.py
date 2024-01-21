import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    email = factory.faker.Faker("email")
    password = factory.faker.Faker("password")

    class Meta:
        model = "users.User"
