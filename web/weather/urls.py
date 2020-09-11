from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('new-city/', views.new_city, name='new-city'),
    path('delete-city/<int:city_id>', views.delete_city, name='delete-city'),
]
