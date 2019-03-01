from django.db import models

def get_image_path(instance, filename):
    return 'stock/{0}/{1}'.format(instance.id, filename)

class Stock(models.Model):
    title = models.CharField(max_length = 20)
    artist = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.name
