from django.urls import path
from projeto_app.views import index, form, list, criar_contato

urlpatterns = [
    path('', index),
    path('form/', form),
    path('list/', list),
    path('form/', criar_contato, name='formulario'),
    
]