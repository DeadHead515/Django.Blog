from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#^^one to many relationship between the user or author and their posts. 

# Create your models here.
#first model is the posts model class. This is the structure of our database for user posts.  
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
#^ this line above deletes the posts a user made if the user is deleted. but it does not delete the user if posts are deleted. 


    def __str__(self):
        return self.title