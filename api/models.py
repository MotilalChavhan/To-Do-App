from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)