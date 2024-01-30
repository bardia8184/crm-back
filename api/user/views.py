import secrets
# from importlib.resources import _
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail, EmailMessage
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import CustomUser
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.template.loader import get_template
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializers


@api_view(['POST'])
def register(req):
    data = req.data
    try:
        CustomUser.objects.create(
            email=data['email'],
            password=make_password(data['password'])
        )
        return JsonResponse({'msg': True})
    except Exception as e:
        # return JsonResponse({'msg': _(e.args[0]), 'type': 'error'})
        return JsonResponse({'msg': '', 'type': 'error'})


# For custom token
class CustomTokenSerializer(TokenObtainPairSerializer):
    # @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.email
        return token


# For custom token
class Login(TokenObtainPairView):
    serializer_class = CustomTokenSerializer
