from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InstagramPost(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    instagram_image = models.ImageField(upload_to='articles/', blank=True)