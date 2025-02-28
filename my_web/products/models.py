from django.db import models

class Category (models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        # ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
         return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

     
class Product(models.Model):
        category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
        brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
        name = models.CharField(max_length=100)
        image = models.ImageField(upload_to='products/')
        price = models. DecimalField(max_digits=10, decimal_places=2)
        new_price = models. DecimalField(max_digits=10, decimal_places=2, default=0)
        on_sale = models.BooleanField(default=False)
        detail = models.TextField(blank=True)
        created_at = models.DateTimeField (auto_created=True)
        
        class Meta:
            ordering = ('name',)
        def __str__(self):
            return self.name
