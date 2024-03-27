from django.db import models
from entreprise.models import Entreprise
class Responsable(models.Model):
    CIVIL_STATUS_CHOICES = [
        ('M.', 'M.'),
        ('Mme.', 'Mme.'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES)
    phone_number = models.CharField(max_length=20)  # Assuming phone number can be stored as a string
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"