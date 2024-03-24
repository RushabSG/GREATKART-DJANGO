from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)
    # blank = true means that the form field can be blank

    def __str__(self) -> str:
        return self.category_name
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"