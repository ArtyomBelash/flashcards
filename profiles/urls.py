from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login', LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('registration', views.CreateProfileView.as_view(), name='registration'),
    path('logout', views.CustomLogoutView.as_view(), name='logout'),
]
