from rabbits_rest.models import Rabbit
from rest_framework import serializers
from os.path import abspath, join


class RabbitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rabbit
        fields = '__all__'

    def validate_Breed(self, value):
        with open(join('rabbits_rest', 'data', 'breeds.txt'), 'r') as f:
            breeds = f.readlines()
        if value.lower() not in [x.lower().strip() for x in breeds]:
            raise serializers.ValidationError("Breed does not exist")
        return value

    def validate_Color(self, value):
        with open(abspath(join('rabbits_rest', 'data', 'colors.txt')), 'r') as f:
            colors = f.readlines()
        if value.lower() not in [x.lower().strip() for x in colors]:
            raise serializers.ValidationError("Color does not exist")
        return value
