from rabbits_rest.models import Rabbit
from rest_framework import serializers


class RabbitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rabbit
        fields = '__all__'
