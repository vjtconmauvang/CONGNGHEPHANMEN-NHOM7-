from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username

class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.species}) - Owner: {self.owner.username if self.owner else 'No owner'}"
