from django.urls import path
from projeto_app.views import index, form

urlpatterns = [
    path('', index),
    path('form/', form),
    
]