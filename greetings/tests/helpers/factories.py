"""Define factories"""
import factory
from ...models import Greeting


class GreetingFactory(factory.django.DjangoModelFactory):
    """Define Greeting factory"""
    class Meta:
        model = Greeting

    message = "arbitrary message"

