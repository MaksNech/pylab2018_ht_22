from django.db import models


# Create your models here.

class Bag(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {}.".format(self.brand, self.title)

    class Meta:
        ordering = ['-created_on']
