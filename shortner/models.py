from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username



class shortURL(models.Model):
    original_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=100)
    time_date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.original_url
