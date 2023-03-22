from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name="заголовок")
    description = models.TextField(max_length=5000, verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name="цена", default=0)
    views_count = models.IntegerField(verbose_name="количество просмотров", default=0)


