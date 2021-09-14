from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Contact(models.Model):
    name = models.CharField(verbose_name='тип контакта', max_length=64)
    city = models.CharField(verbose_name='название города', max_length=64)
    phone = models.CharField(verbose_name='номер телефона', max_length=16)
    email = models.EmailField(verbose_name='email адресс', blank=True)
    address = models.CharField(verbose_name='адресс', max_length=254)

    def __str__(self):
        return self.name

