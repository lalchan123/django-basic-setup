from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



# Create your views here.
@api_view(['GET'])
def HelloWorld(request):
    try:
        return Response({'message':"success", "data": "hello world"})
    except Exception:
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'message':f'Something errors'})  
        