import factory.fuzzy
from faker import Faker
from .models import Post, Comment
from user.factories import UserFactory

faker = Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda _: faker.sentence())
    author = factory.SubFactory(UserFactory)
    post_text = factory.Faker("text", max_nb_chars=200)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.SubFactory(UserFactory)
    comment_text = factory.Faker("sentence", nb_words=10)
    post = factory.SubFactory(PostFactory)
