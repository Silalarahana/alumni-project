from django.db import models

# Create your models here.


class Alumni(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    graduation_year = models.IntegerField()
    company = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.message

from django.db import models

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    company = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    # NEW FIELDS
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
