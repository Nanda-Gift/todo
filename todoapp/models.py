from django.db import models

# Create your models here.
class todolist(models.Model):
    text = models.TextField()
    email = models.EmailField()



