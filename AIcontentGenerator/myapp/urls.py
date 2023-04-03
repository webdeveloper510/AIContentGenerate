from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index1),
    path('generate/', views.content_generate),
]
