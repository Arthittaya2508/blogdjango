from django.db import models
from category.models import Category

# Create your models here.
class Blogs(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Content = models.TextField()
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Writer = models.CharField(max_length=255)
    View = models.IntegerField(default=0)
    Image = models.ImageField(upload_to="BlogImage",blank=True)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
