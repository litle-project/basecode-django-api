import bcrypt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, UserSaveSerializer
from django.core import serializers

@api_view(['GET'])
def index(request):
    try:
        keyword = request.query_params.get('keyword', '')
        users = User.objects.filter(Q(name__contains=keyword) | Q(email__contains=keyword))
        
        if users:
            serializer = UserSerializer(users, many=True)
            return Response({'code': 200, 'message': 'OK', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'code': 404, 'message': 'No Content', 'data': []}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        return Response({'code': 500, 'message': str(error), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        
        if user:
            serializer = UserSerializer(user)
            return Response({'code': 200, 'message': 'OK', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'code': 404, 'message': 'No Content', 'data': None}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        return Response({'code': 500, 'message': str(error), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create(request):
    try:
        paramter = request.data
        
        serializer = UserSaveSerializer(data=paramter)
        if not serializer.is_valid():
            return Response({'code': 422, 'message': serializer.errors, 'data': None}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        user = User(
            name=paramter.get('name'),
            email=paramter.get('email'),
            password=bcrypt.hashpw(paramter.get('password').encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            description=paramter.get('description')
        )

        user.save()

        return Response({'code': 200, 'message': 'OK', 'data': None}, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'code': 500, 'message': str(error), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def update(request, pk):
    try:
        paramter = request.data
        
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=paramter)
        
        if not serializer.is_valid():
            return Response({'code': 422, 'message': serializer.errors, 'data': None}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        User.objects.filter(pk=pk).update(
            name=paramter.get('name'),
            email=paramter.get('email'),
            description=paramter.get('description')
        )

        return Response({'code': 200, 'message': 'OK', 'data': None}, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'code': 500, 'message': str(error), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['DELETE'])
def delete(request, pk):
    try:
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({'code': 200, 'message': 'OK', 'data': None}, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'code': 500, 'message': str(error), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)