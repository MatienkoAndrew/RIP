from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.main, name='main'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	url(r'^login/', views.LoginForm.as_view(), name='login'),
	url(r'^logout/', views.LogoutForm.as_view(), name="logout"),
	url(r'^registration/', views.RegistrationForm.as_view(), name="registration"),
	url(r'^profile/', views.user_profile, name="profile"),
	path(r'^profile/edit/', views.edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
