from django.db import models


class Todo(models.Model):
    body = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

