from rest_framework import serializers

from application.simple_information.models import Category, Car


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CarSerializers(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['model', 'year', 'category']
