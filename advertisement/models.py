from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name="заголовок", db_index=True)
    description = models.TextField(max_length=5000, verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name="цена", default=0)
    views_count = models.IntegerField(verbose_name="количество просмотров", default=0)
    status = models.ForeignKey("AdvertisementStatus", default=None, null=True, on_delete=models.CASCADE,
                               related_name="advertisements")
    region = models.ManyToManyField("Region")
    type = models.ForeignKey("AdvertisementType", default=None, null=True, on_delete=models.CASCADE,
                             related_name="advertisements")


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)


class Region(models.Model):
    name = models.CharField(max_length=200)


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)


