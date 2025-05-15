from django.db import models
from authentication.models import Profile
from authentication.models import BaseModel


class AssignedUsers(BaseModel):
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='admin_users')
    users=models.ManyToManyField(Profile, related_name='assigned_userss')


    class Meta:
        verbose_name = 'Assigned User'
        verbose_name_plural = 'Assigned Users'


class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks_assigned',null=True, blank=True)
    completion_report=models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50,null=True, blank=True)
    due_date = models.DateTimeField()
    worked_hours = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='created_by',null=True, blank=True)



    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at']

