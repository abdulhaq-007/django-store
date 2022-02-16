from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Name", max_length=50)
    slug = models.SlugField("*", max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Category"


class BannerHeader(models.Model):
    banner = models.ImageField('Banner Rasmi', upload_to='images/banner/')
    title = models.CharField('Title', max_length=255)
    body = models.TextField('Body')
    footer = models.CharField('Footer', max_length=255)
    url = models.CharField('Url', max_length=40000)


class BannerBody(models.Model):
    banner = models.ImageField('Banner Rasmi', upload_to='images/banner/')
    title = models.CharField('Title', max_length=255)
    body = models.TextField('Body')
    footer = models.CharField('Footer', max_length=255)
    url = models.CharField('Url', max_length=40000)



class Colors(models.Model):
	COLORS = (
	('white','WHITE'),
	('black','BLACK'),
	('blue','BLUE'),
	('green','GREEN'),
	('yellow','YELLOW'),
	('red','RED'),
	('tomato','TOMATO'),
	('pink','PINK'),
	('teal','TEAL'),
	('brown','BROWN'),
	)
	color = models.CharField('Product Color', max_length=50, choices=COLORS)
	def __str__(self):
		return self.color

class Product(models.Model):
    COLORS = (
        ('white', 'WHITE'),
        ('black', 'BLACK'),
        ('blue', 'BLUE'),
        ('green', 'GREEN'),
        ('yellow', 'YELLOW'),
        ('red', 'RED'),
        ('tomato', 'TOMATO'),
        ('pink', 'PINK'),
        ('teal', 'TEAL'),
        ('brown', 'BROWN'),
    )
    name = models.CharField("Name", max_length=100)
    slug = models.SlugField("*", max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
        )
    image = models.ImageField("Product image", upload_to='product_images/')
    price = models.PositiveIntegerField("Price", default=0)
    description = models.TextField("About product")
    in_stock = models.PositiveIntegerField("Count", default=1)
    colors = models.ManyToManyField(Colors, related_name="colors", null=True, blank=True)
    discount = models.CharField("Discount", max_length=10, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-id"]



# Product Images model
class ProductImages(models.Model):
	product = models.ForeignKey(Product,
		default=None,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='product_images')
	image = models.ImageField('SLider Image',
		upload_to='product_images/',
		blank=True, null=True,)

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = 'Slider Images'
		verbose_name_plural = 'Slider Image'


class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()


    def __str__(self):
        return self.name


