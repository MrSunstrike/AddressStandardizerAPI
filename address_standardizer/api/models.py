from django.db import models

class AddressStandardization(models.Model):
    request = models.CharField(max_length=60)
    result = models.TextField(blank=True, null=True)
