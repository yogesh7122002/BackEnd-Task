# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('submit_request/', views.submit_request, name='submit_request'),
    path('request_success/', views.request_success, name='request_success'),
    path('view_requests/', views.view_request, name='view_requests'),
]
