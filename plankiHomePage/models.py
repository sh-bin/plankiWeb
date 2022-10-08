from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='Адрес электронной почты', null=True, blank=True, unique=True)
    phone = models.BigIntegerField(verbose_name='Телефонный номер', null=True, blank=True)
    country = models.CharField(max_length=120, verbose_name='Страна', null=True, blank=True)
    region_area = models.CharField(max_length=120, verbose_name='Регион / Область', null=True, blank=True)
    city = models.CharField(max_length=120, verbose_name='Город', null=True, blank=True)
    address1 = models.CharField(max_length=250, verbose_name='Адрес', null=True, blank=True)
    address2 = models.CharField(max_length=250, verbose_name='Дополнительный адрес', null=True, blank=True)
    index = models.BigIntegerField(verbose_name='Индекс', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['country', 'username']


# class ReviewsSlats(models.Model):
#     user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
#     product = models.ForeignKey('Slats', on_delete=models.CASCADE, verbose_name='Товар')
#     content = models.CharField(max_length=350, verbose_name='Отзыв')
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
#     updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
#     active = models.BooleanField(default=True, verbose_name='Показывается')
#
#     class Meta:
#         verbose_name = 'Отзыв о планке'
#         verbose_name_plural = 'Отзывы о планках'
#         ordering = ['created', 'product']
#
#     def __str__(self):
#         return f'Комментарий {self.user}'


class CategorySlats(models.Model):
    name = models.CharField(max_length=170, db_index=True, verbose_name='Название')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.SlugField(max_length=170, unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию Планок'
        verbose_name_plural = 'Категории Планок'
        ordering = ['time_create', 'name']

    def get_absolute_url(self):
        return reverse('plankiHomePage:slats', kwargs={'slug_id': self.slug})


class Slats(models.Model):
    name = models.CharField(max_length=170, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=170, unique=True, verbose_name='Слаг')
    description = models.TextField(max_length=300, verbose_name='Описание')
    category = models.ForeignKey('CategorySlats', on_delete=models.PROTECT, verbose_name='Категория')
    image = models.ImageField(upload_to='plankiHomePage/images/slats/%Y/%m/%d', blank=True, verbose_name='Фото')
    stock = models.PositiveIntegerField(verbose_name='Остаток продукта')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Планка'
        verbose_name_plural = 'Планки'
        ordering = ['time_create', 'name']

    def get_absolute_url(self):
        return reverse('plankiHomePage:detail_slats', kwargs={'slug_id': self.slug})


class Sashes(models.Model):
    name = models.CharField(max_length=170, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=170, unique=True, verbose_name='Слаг')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='plankiHomePage/images/sashes/%Y/%m/%d', blank=True, verbose_name='Фото')
    stock = models.PositiveIntegerField(verbose_name='Остаток продукта')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лента'
        verbose_name_plural = 'Ленты'
        ordering = ['time_create', 'name']

    def get_absolute_url(self):
        return reverse('plankiHomePage:detail_sashes', kwargs={'slug_id': self.slug})


class Jettons(models.Model):
    name = models.CharField(max_length=170, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=170, unique=True, verbose_name='Слаг')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='plankiHomePage/images/jettons/%Y/%m/%d', blank=True, verbose_name='Фото')
    stock = models.PositiveIntegerField(verbose_name='Остаток продукта')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жетон'
        verbose_name_plural = 'Жетоны'
        ordering = ['time_create', 'name']

    def get_absolute_url(self):
        return reverse('plankiHomePage:detail_jettons', kwargs={'slug_id': self.slug})
