from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/',default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @classmethod
    def update_profile(cls, id, value):
        cls.objects.filter(id=id).update(profile=value)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.name

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

# Create your models here.
class InstagramPost(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='posts', null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/', blank=True) 

    @classmethod
    def get_Profile(cls, user):
        profile = InstagramPost.objects.filter(user__user=user).all()
        return profile

    def save_image(self):
        self.save()
    
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def update_caption(cls, id, value):
        cls.objects.filter(id=id).update(description=value)

    def delete_image(self):
        self.delete()

    def __str__(self):
        return f'{self.user.name} Post'

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(InstagramPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'

 

