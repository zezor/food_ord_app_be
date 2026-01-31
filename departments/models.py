from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    college = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
