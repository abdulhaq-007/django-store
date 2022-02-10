from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Name", max_length=50)
    slug = models.SlugField("*", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"

class Cat(models.Model):
    name = models.CharField("Name", max_length=50)
    slug = models.SlugField("*", max_length=50)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='cats')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Cats"        

class Product(models.Model):
    name = models.CharField("Name", max_length=100)
    slug = models.SlugField("*", max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
        )
    image = models.ImageField("Product image", upload_to='product_images/')
    old_price = models.PositiveIntegerField("Old price", default=0)
    price = models.PositiveIntegerField("Price", default=0)
    in_stock = models.PositiveIntegerField("Nechchi kg ombor", default=0)
    quantity = models.PositiveIntegerField("Nechchi kg kerak", default=0)

    def __str__(self):
        return f"{self.name}"