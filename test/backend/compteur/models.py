from django.db import models
from entreprise.models import Entreprise

class Compteur(models.Model):
    ENTRE_CHOICES = [
        ('ELEC', 'Electricity'),
        ('GAZ', 'Gas'),
    ]
    pdl = models.CharField(max_length=14, unique=True)
    entre = models.CharField(max_length=10, choices=ENTRE_CHOICES)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    def __str__(self):
        return f"Compteur {self.pdl} - {self.entre} ({self.entreprise})"