from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tindak_pidana', views.tindak_pidana, name='tindak_pidana'),
    path('tindak_pidana/create/', views.create, name='create'),
    path('tindak_pidana/edit/', views.edit, name='edit'),
    path('tindak_pidana/delete/(?P<id_TP>\d+)$', views.delete, name='delete'),

]