from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY = (
    ('All Recipes', "All Recipes"),
    ('Vegan', "Vegan"),
    ('Chocolate Recipes', "Chocolate Recipes"),
    ('Fruits', "Fruits"),
    ('Gluten Free', "Gluten Free"),
    ('Birthday & Wedding', "Birthday & Wedding"),
    ('Christmas Recipes', "Christmas Recipes"),
)

DIFICULTY = (
    ('Easy', "Easy"),
    ('Medium', "Medium"),
    ('Hard', "Hard"),
)


class Recipe(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_recipe")
    category = models.CharField(max_length=20, choices=CATEGORY, default='all')
    dificulty = models.CharField(max_length=10, choices=DIFICULTY, default='Easy')
    total_time = models.IntegerField(default=60)
    created_recipe = models.DateTimeField(auto_now_add=True)
    updated_recipe = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    featured_image = CloudinaryField("image", default='placeholder')
    exerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
        


