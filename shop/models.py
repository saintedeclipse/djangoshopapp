from django.db import models
from django.utils import timezone
# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length=255)
    date_of_creation = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
""" Создана модель для категорий, в ней 1 строка - заголовок, 2 строка
Дата создания категории, она выводится в скобках используя
timezone.now, предварительно импортировав timezone из django.utils """

class Course(models.Model):
    title = models.CharField(max_length=300)
    date_of_creation = models.DateTimeField(default = timezone.now)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

"""Создан 2ой курс, с ним вероятно всё понятно кроме последнего столбца
 это строка категория из класса Category, в которой содержится наименование
 категории, параметр on.delete  удаляет запись КУРСА если удалена КАТЕГОРИЯ"""