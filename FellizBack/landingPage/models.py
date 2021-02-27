from django.db import models


class ClientCoffe(models.Model):
    firstname = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.IntegerField()
    reviews = models.TextField()

    def __str__(self):
        return self.firstname
