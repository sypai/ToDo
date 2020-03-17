from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=300)
    todo_date = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=50)
    user_id = models.IntegerField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
