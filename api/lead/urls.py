from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

urlpatterns = [
    path('new_lead/', views.new_lead),
    path('all_leads/', views.get_all_leads),
]
