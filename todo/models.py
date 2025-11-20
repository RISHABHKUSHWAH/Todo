from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=15)
    memo = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title