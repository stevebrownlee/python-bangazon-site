from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        context = {
            "id": self.id
        }
        return reverse("website:detail", kwargs=context)
