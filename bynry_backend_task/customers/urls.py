# urls.py

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),  # Home page URL
    # path('submit_request/', views.submit_request, name='submit_request'),
    # path('request_success/', views.request_success, name='request_success'),
    # path('view_requests/', views.view_request, name='view_requests'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home, name='home'),
    path('request_success/', views.request_success, name='request_success'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('view_requests/', views.view_request, name='view_requests'),
    path('profile/', views.profile, name='profile'),
]
