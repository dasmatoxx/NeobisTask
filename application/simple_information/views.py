from django.shortcuts import render
from rest_framework.generics import ListAPIView

from application.simple_information.models import Category, Car
from application.simple_information.serializers import CategorySerializers, CarSerializers


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CarView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
