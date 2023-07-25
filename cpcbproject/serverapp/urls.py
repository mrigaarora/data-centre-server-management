from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('search',views.search,name='search'),
    path('com',views.com,name="com"),
    path('apps',views.apps,name='apps'),
    path('edit/<int:edit_id>/', views.edit, name='edit'),
    path('searchbar', views.searchbar,name='searchbar' ),
    path('edit_S/<int:edit_id>/', views.edit, name='edit'),
    path('create_superuser/', views.create_superuser, name='create_superuser'),
     path('check_password/', views.check_password, name='check_password'),
]