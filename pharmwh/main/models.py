from django.db import models

class Products(models.Model):
    title = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Номенклатура'
