from rest_framework import serializers
from places import models as modpl


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = modpl.Place
        fields = '__all__'






class PlaceMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = modpl.PlaceMedia
        fields = '__all__'
