from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crudcreate', views.crudcreate, name='crudcreate'),
    path('crudupdate/<int:id>', views.crudupdate, name='crudupdate'),

    path('cruddelete/<int:id>', views.crudDelete, name='crudDelete'),
]