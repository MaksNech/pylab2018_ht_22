from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save


# Create your models here.

class Bag(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='bags/', blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {}.".format(self.brand, self.title)

    class Meta:
        ordering = ['-created_on']

# SIGNALS:  ############################################################################################################
# Begin

# delete img with bag instance
@receiver(post_delete, sender=Bag)
def bag_img_delete(sender, instance, **kwargs):
    instance.image.delete(False)

# End
########################################################################################################################