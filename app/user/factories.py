import factory.fuzzy
from django.contrib.auth import get_user_model
from faker import Faker

faker = Faker()
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = factory.LazyAttribute(lambda _: faker.user_name())
    first_name = factory.LazyAttribute(lambda _: faker.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.last_name())
    email = factory.LazyAttribute(lambda _: faker.email())
    # пароль будет задан тестовый для всех созданных пользователей
    # в базу данных будет сохранен в хэшированном виде
    password = factory.PostGenerationMethodCall("set_password",
                                                "testpassword"
                                                )
