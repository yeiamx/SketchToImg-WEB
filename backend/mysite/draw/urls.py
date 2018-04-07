from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edges2bag', views.edges2bag, name='edges2bag')
]