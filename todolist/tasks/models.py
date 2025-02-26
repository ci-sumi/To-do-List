from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    complted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return self.title
  
    

# Create your models here.
