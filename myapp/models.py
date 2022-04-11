from django.db import models


class Discipline(models.Model):
    name = models.CharField('Название дисциплины', max_length=200)
    description = models.TextField('Описание дисциплины', max_length=5000)
    average = models.CharField('Средний балл группы', max_length=200)
    total = models.CharField('Максимальное количество баллов', max_length=200)

    class Meta:
        verbose_name = 'Дисциплину'
        verbose_name_plural = 'Дисциплины'