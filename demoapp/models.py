from django.db import models
from datetime import datetime

# Create your models here.
"""class Blog(models.Model):
    title=models.CharField(max_length=100)
    #images
    image=models.ImageField(upload_to="images/")
    #videos
    video=models.FileField(upload_to="media/",null=True)
    description=models.TextField() 
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title"""

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField() 
    image=models.ImageField(upload_to="images/",null=True)
    created_at=models.DateTimeField(default=datetime.now)
    is_resolved=models.BooleanField(default=False)

    def __str__(self):
        return self.name