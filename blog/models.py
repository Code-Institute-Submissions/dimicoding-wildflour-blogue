from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY = (
    (0, "All Recipes"),
    (1, "Vegan"),
    (2, "Chocolate Recipes"),
    (3, "Fruits"),
    (4, "Gluten Free"),
    (5, "Birthday and Wedding"),
    (6, "Christmas Recipes"),
)
DIFICULTY = (
    (0, "Easy"),
    (1, "Medium"),
    (2, "Hard"),
)


class Recipe(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_recipe")
    category = models.IntegerField(choices=CATEGORY, default=0)
    dificulty = models.IntegerField(choices=DIFICULTY, default=0)
    total_time = models.IntegerField(default=60)
    created_recipe = models.DateTimeField(auto_now_add=True)
    updated_recipe = models.DateTimeField(auto_now=True)
    body = models.TextField()
    featured_image = CloudinaryField("image", default='placeholder')
    exerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
