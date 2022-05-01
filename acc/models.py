from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pic = models.ImageField(upload_to="user/%y/%m/%d")
    comment = models.TextField()
    age = models.IntegerField(default=1)

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/user/no_image.png"