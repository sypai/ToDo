from django.db import models
from datetime import datetime


# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=300)
    todo_date = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=50)
    user_id = models.IntegerField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
