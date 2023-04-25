from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

DIFICULTY = (
    ('Easy', "Easy"),
    ('Medium', "Medium"),
    ('Hard', "Hard"),
)


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField("image", default='placeholder')
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


class Recipe(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default="all")
    dificulty = models.CharField(max_length=10, choices=DIFICULTY, default='Easy')
    total_time = models.IntegerField(default=60)
    created_recipe = models.DateTimeField(auto_now_add=True)
    updated_recipe = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    featured_image = CloudinaryField("image", default='placeholder')
    exerpt = models.TextField(max_length=150, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    
    def number_likes(self):
        return self.likes.count()
        

class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.post.title} by {self.name}'
