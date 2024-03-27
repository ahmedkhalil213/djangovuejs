from django.db import models
from users.models import CustomUser

class Entreprise(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    raison = models.CharField(max_length=255)
    siret = models.CharField(max_length=14, unique=True)
    adresse_postale = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.raison} - {self.siret}"
