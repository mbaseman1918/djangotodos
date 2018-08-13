from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('remove/<int:pk>/', views.remove, name='remove'),
    path('done/<int:pk>/', views.done, name='done'),
    path('add/', views.add, name='add'),
    path('', views.index, name='index'),
]
