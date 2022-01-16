from rest_framework import serializers
from foods.models import Food

class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
