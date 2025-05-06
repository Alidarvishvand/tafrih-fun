from rest_framework import serializers
from interactions import models as intmodel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = intmodel.Comment
        fields = '__all__'
        read_only_fields = ['user', 'created_at']


class RatingSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(min_value=1, max_value=5)  

    class Meta:
        model = intmodel.Rating
        fields = '__all__'
        read_only_fields = ['user', 'created_at']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = intmodel.Favorite
        fields = '__all__'
        read_only_fields = ['user', 'created_at']
