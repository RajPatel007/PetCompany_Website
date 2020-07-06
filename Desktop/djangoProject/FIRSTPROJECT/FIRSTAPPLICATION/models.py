from django.db import models


class Candidate(models.Model):
    name = models.CharField(unique=False, max_length=50)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


