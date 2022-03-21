from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from store.models import Users
from store.serializers import UserSerialiser

from  rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.

def index(request):
    return JsonResponse('Login..')


@api_view(['GET'])
def getUser(request):
    if request.method == 'GET':
        users =  Users.objects.all()
        userSerialiser = UserSerialiser(users, many = True)
        return JsonResponse(userSerialiser.data, safe=False)

@api_view(['GET'])
def getUserById(request, id):
    try:
        users = Users.objects.get(pk= id)
    except Users.DoesNotExist:
        return JsonResponse({"Message":"User not found"})

    if request.method == 'GET':
        # users =  Users.objects.all()
        userSerialiser = UserSerialiser(users)
        return JsonResponse(userSerialiser.data, safe=False)

   
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        users = JSONParser().parse(request)
        userSerialiser = UserSerialiser(data=users)
        if userSerialiser.is_valid():
            userSerialiser.save()
            return JsonResponse(userSerialiser.data, status=status.HTTP_201_CREATED)
        return JsonResponse(userSerialiser.errors, status=status.HTTP_400_BAD_REQUEST)
