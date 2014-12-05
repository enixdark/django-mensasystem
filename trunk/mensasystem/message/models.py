from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField()
    message = models.TextField(blank=True,null=True)


