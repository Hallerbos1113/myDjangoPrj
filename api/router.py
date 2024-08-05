from django.urls import path
from . import controller

urlpatterns = [
    path('test', controller.getTest),
    path('testPost/<str:name>', controller.getPost)
]