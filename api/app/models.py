from django.db import models

class UserRegistration(models.Model):
    roll_no = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    pwd = models.CharField(blank=False, max_length=50)
    image = models.ImageField(upload_to='images/')  # Specify the correct 'upload_to' path

    def __str__(self):
        return self.name
