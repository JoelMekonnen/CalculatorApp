from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ResultHistory(models.Model):
    #this model defines the history of the user calculations
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="result")
    expression = models.CharField(max_length=500, null=True)
    result = models.CharField(max_length=500, null=True)

