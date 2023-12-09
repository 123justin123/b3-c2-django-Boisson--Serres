from django.db import models
from django.contrib.auth.models import User


class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    url = models.URLField()
    identifiant = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
