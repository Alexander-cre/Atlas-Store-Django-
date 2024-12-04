from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=15, blank=True , null=True)
    address = models.TextField(blank=True , null=True )
    city = models.TextField(max_length=15, blank=True , null=True)
    sex = models.TextField(max_length=15, blank=True , null=True )

    def __str__(self):
        return self.user.username
    


@ receiver(post_save , sender=User )
def create_user(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user=instance)   

@receiver(post_save , sender=User)
def save_profile(sender , instance , **kwargs):
    instance.profile.save()