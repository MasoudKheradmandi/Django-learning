from rest_framework import generics
from .serializers import (RegistrationsSerializers , CustomAuthTokenSerializer,
                SerializersProfile,ResendVerificationsSerializers )
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ...models import Profile
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.conf import settings


User = get_user_model()

class RegestrationsApiView(generics.GenericAPIView):
    serializer_class = RegistrationsSerializers



    def post(self, request, *args, **kwargs):
        serializer = RegistrationsSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {
                'email':email
                }
            user_obj = get_object_or_404(User,email=email)
            token = self.get_tokens_for_user(user_obj)
            send_mail (
            'Subject here',
            f"http://127.0.0.1:8000/accounts/api/v1/active/token/{token}",
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
            )
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)




class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class RevortToken(APIView):
    permission_classes = [IsAuthenticated]


    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfile(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = SerializersProfile

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset,user=self.request.user)
        return obj

class SendEmail(generics.GenericAPIView):

    def post(self,request,*args,**kwargs):
        self.email = "test@test.com"
        user_obj = get_object_or_404(User,email=self.email)
        token = self.get_tokens_for_user(user_obj)

        send_mail (
        'Subject here',
        token,
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
        )
        return Response("Done")

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)

class ActivationsApiView(APIView):
    
    def get(self,request,token,*args, **kwargs):
        
        try:
            token = jwt.decode(token,settings.SECRET_KEY , algorithms=["HS256"])
            user_id = token.get("user_id")
        except ExpiredSignatureError:
            return Response(
                {"details": "token has been expired"},status=status.HTTP_400_BAD_REQUEST,)
        except InvalidSignatureError:
            return Response(
                {"details": "token is not valid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_obj = User.objects.get(pk=user_id)
        if user_obj.is_verified:
            return Response({"details": "your account has already been verified"})
        user_obj.is_verified = True
        user_obj.save()
        return Response(
            {"details": "your account have been verified and activated successfully"}
        )


class ResendVerfications(generics.GenericAPIView):
    serializer_class = ResendVerificationsSerializers

    def post(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = self.get_tokens_for_user(user)
        send_mail (
        'Subject here',
        f"http://127.0.0.1:8000/accounts/api/v1/active/token/{token}",
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
        )
        return Response(
            {"details": "user activation resend successfully"},
            status=status.HTTP_200_OK,
        )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)