from rest_framework.response import Response
from rest_framework.views import APIView
from dashboard.models import Task
from .serializers import TaskSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from authentication.permissions import *

class TaskListAPIView(APIView):
    permission_classes = [IsUser]
    def get(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)
        if not tasks.exists():
            return Response({'message': 'No tasks found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class TaskStatusUpdateAPIView(APIView):
    permission_classes = [IsUser]
    def put(self, request, task_id):
        task = get_object_or_404(Task, uuid=task_id)
        task_status=request.data.get('status')
        if not task_status:
            return Response({'error': 'Task status is required'}, status=400)
        task.status = task_status
        task.save()
        return Response({'message': 'Task status updated successfully'}, status=status.HTTP_200_OK)
    
    def get(self, request, task_id):
        task =get_object_or_404(Task,uuid=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SubmitTaskReportAPIView(APIView):
    permission_classes = [IsUser]
    def post(self, request, task_id):
        task = get_object_or_404(Task, uuid=task_id)
        report=request.data.get('completion_report')
        if not report:
            return Response({'error': 'Completion report is required'}, status=400)
        task.completion_report = request.data.get('completion_report')
        task.save()
        return Response({'message': 'Task report submitted successfully'}, status=200)