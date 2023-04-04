from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "For Sale"), (1, "Sold"))


class Listing(models.Model):
    address = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listing_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='listing_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.address

    def number_of_likes(self):
        return self.likes.count()


class Feature(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="features")
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    ber_category = models.TextField()
    price = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
