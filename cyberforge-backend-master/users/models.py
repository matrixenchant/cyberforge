from django.db import models
from django.contrib.auth.models import AbstractUser
from configurator.models import Modification


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='users_image', null=True, blank=True)
    modifications = models.ManyToManyField(Modification, blank=True)

    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users_user'


# class CustomModification(models.Model):
#
#     modification = models.ForeignKey(Modification, on_delete=models.CASCADE)
#     users = models.ManyToManyField(User, blank=True)





