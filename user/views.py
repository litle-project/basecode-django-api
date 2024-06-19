from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.db.models import Q
from .serializers import UserSerializer

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