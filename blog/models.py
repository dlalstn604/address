from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
from django.utils import timezone


class Address(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    home_number = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name