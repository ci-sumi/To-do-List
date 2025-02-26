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
    serieliazer = TaskSerializer(tasks,many=True)
    return Response(serieliazer.data)
    
