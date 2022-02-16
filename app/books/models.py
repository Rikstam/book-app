from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class CustomUser(AbstractUser):
    pass
class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    publishers = models.ManyToManyField(Publisher)
    number_of_pages = models.PositiveIntegerField(default=1)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)