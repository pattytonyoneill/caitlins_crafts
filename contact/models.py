from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
