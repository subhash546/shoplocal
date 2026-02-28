from django.db import models

# Create your models here.

class Category (models.Model):
    category_name=models.CharField(max_length=66,blank=False)
    slug=models.SlugField(max_length=100,blank=False,unique=True)
    description=models.TextField(max_length=200,blank=True)
    cat_img=models.ImageField(upload_to='photos/category')
    
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
    
    
    def __str__(self):
        return self.category_name