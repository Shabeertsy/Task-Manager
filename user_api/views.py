from rest_framework.response import Response
from rest_framework.views import APIView
from dashboard.models import Task
from .serializers import TaskSerializer

from authentication.permissions import *

class TaskListAPIView(APIView):
    permission_classes = [IsUser]
    def get(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data,status=200)
    

class TaskStatusUpdateAPIView(APIView):
    permission_classes = [IsUser]
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.status = request.data.get('status')
        task.save()
        return Response({'message': 'Task status updated successfully'}, status=200)
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=200)

class SubmitTaskReportAPIView(APIView):
    permission_classes = [IsUser]
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.completion_report = request.data.get('completion_report')
        task.save()
        return Response({'message': 'Task report submitted successfully'}, status=200)