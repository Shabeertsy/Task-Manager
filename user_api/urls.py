from django.urls import path
from . import views

urlpatterns = [
    path('my_tasks/', views.TaskListAPIView.as_view(), name='task-list'),
    path('submit_task_report/<int:task_id>/', views.SubmitTaskReportAPIView.as_view(), name='submit-task-report'),
    path('update_task_status/<int:task_id>/', views.TaskStatusUpdateAPIView.as_view(), name='update-task-status'),
    
]
