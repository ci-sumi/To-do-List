from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import TaskSerializer
# Create your views here.
#Retrieve all tasks
@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def  task_create(request):
    serializer = TaskSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    
