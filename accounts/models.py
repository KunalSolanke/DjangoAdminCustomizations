from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import UserManager
from django.conf import settings
# Create your models here.





#Task_1

'''
   Changed superuser
'''

mailing_list = []

class User(AbstractUser) :
    username = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    objects = UserManager()

    def __str__(self):
        return self.username



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def add_to_mailing_list(sender,instance,created,**kwargs) :
    if created :
        mailing_list.append(instance.email)


