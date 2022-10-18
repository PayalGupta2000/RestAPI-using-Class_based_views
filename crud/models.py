from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    image=models.URLField()
    product_description=models.TextField()
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE,default=True)

    def __str__(self):
        return self.product_name