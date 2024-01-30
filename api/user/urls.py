from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='token_obtain_pair'),
    path('register/', views.register, name='register'),
    path('check-auth/', TokenVerifyView.as_view(), name='token_verify'),
]
