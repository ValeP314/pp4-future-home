from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from datetime import datetime


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
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    ber_category = models.CharField(max_length=3)
    price = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='listing_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.address

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')


class Question(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="questions")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Question {self.body} by {self.name}"

    def total_questions(self):
        return question.count


class Answer(models.Model):
    question = models.OneToOneField(
        Question, on_delete=models.CASCADE, related_name="answer")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="answers")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Answer to {self.question}: {self.body}"
