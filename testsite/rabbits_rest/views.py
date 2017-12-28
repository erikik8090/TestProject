from rabbits_rest.models import Rabbit
from rabbits_rest.serializers import RabbitSerializer
from rest_framework import viewsets


class RabbitViewSet(viewsets.ModelViewSet):
    serializer_class = RabbitSerializer
    queryset = Rabbit.objects.all()
