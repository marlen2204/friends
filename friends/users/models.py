from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    id = models.AutoField(auto_created=True, primary_key=True)
    
