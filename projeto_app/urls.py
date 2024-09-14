from django.urls import path
from projeto_app.views import index, form, list

urlpatterns = [
    path('', index),
    path('form/', form, name='form'),
    path('list/', list),

]
