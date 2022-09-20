from django.db import models


class Welcome(models.Model):
    sentence = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.sentence
