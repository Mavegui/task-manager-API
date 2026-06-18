from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """
    The model Task is simple and direct.
    
    Attribbutes:
        - FK user in cascade.
        - class Priority (Lower, Medium, High), support priority field.
        - title
        - description
        - priority selection field, where it is called the Priority class
        - completed, where false is the default, when create.
        - Date Field created and updated the model Task. 
    
    class Meta, the ordering based in created at date.
    The last field is the function return str.  
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    
    class Priority(models.TextChoices):
        LOW = 'L', 'Lower'
        MEDIUM = 'M', 'Medium'
        HIGH = 'H', 'High'
    
    title = models.CharField(max_length=255)
    description = models.TextField()    
    priority = models.CharField(
        max_length=1, 
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return f"{self.title} ({self.get_priority_display()})"