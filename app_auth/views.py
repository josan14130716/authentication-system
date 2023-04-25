from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RegisteredUser

# Create your views here.
class Register(APIView):

    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user_dict = {
            'username':username,
            'password':password
        }
        RegisteredUser.objects.create(
            user_name = username,
            password = password 
        )

        return Response(user_dict)
class Login(APIView):
    def post(self,request):
        return Response('login success')
