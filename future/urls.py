from django.urls import path
from . import views

urlpatterns = [
    # General Pages
    path('', views.main_content_view, name='home'),
    path('path/', views.view_path_view, name='view_path'),
    path('progress/', views.progress_view, name='progress'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    # Dynamic Content
    path('content/<str:content_type>/', views.dynamic_content_view, name='dynamic_content'),
]
