from django.urls import path
from projeto_app.views import index, form, list, edit

urlpatterns = [
    path('', index),
    path('form/', form, name='form'),
    path('list/', list, name='list'),
    path('edit/<int:contato_id>/', edit, name='edit')

]
