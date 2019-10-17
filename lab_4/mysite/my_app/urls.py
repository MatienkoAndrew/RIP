from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	url(r'^$', views.get_list, name='get_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
]