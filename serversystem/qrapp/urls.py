from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search,name='search'),
    path('com',views.com,name="com"),
    path('comedit',views.comedit,name='comedit'),
    path('apps',views.apps,name='apps'),
    path('edit/<int:edit_id>/', views.edit, name='edit'),
]