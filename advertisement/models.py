from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория")

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name="заголовок", db_index=True)
    description = models.TextField(max_length=5000, verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name="цена", default=0)
    views_count = models.IntegerField(verbose_name="количество просмотров", default=0)
    status = models.ForeignKey("AdvertisementStatus", default=None, null=True, on_delete=models.CASCADE,
                               related_name="advertisements", verbose_name="Статус")
    region = models.ManyToManyField("Region", verbose_name="Регионы")
    type = models.ForeignKey("AdvertisementType", default=None, null=True, on_delete=models.CASCADE,
                             related_name="advertisements", verbose_name="Тип")
    category = models.ForeignKey("AdvertisementCategory", default=None, null=True, on_delete=models.CASCADE,
                                 related_name="advertisements", verbose_name="Категория")
    author = models.ForeignKey("Author", on_delete=models.CASCADE, default=None, null=True, related_name="advertisements",
                               verbose_name="Автор")


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


