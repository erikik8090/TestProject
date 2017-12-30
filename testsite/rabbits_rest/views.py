from django_filters.rest_framework import DjangoFilterBackend
from rabbits_rest.models import Rabbit
from rabbits_rest.serializers import RabbitSerializer
from rest_framework import viewsets


class RabbitViewSet(viewsets.ModelViewSet):
    serializer_class = RabbitSerializer
    queryset = Rabbit.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('Color', 'Nickname', 'Age', 'Breed')
