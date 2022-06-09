from django.urls import path

from application.simple_information.views import CategoryView, CarView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('car/', CarView.as_view()),
]
