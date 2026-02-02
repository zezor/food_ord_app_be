from django.db import models



class College(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='departments',null=True , blank=True)
    contact_person = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name