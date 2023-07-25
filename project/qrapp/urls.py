from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search,name='search'),
    path('com',views.com,name="com"),
    path('apps',views.apps,name='apps'),
]