from django.core.validators import FileExtensionValidator
from django.db import models

from user.models import AdvUser


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name


class Application(models.Model):
    STATUSES = [
        ('new', 'Новая'),
        ('in_work', 'В работе'),
        ('complete', 'Выполнено')
    ]

    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Создатель')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(verbose_name='Изображение', upload_to='application_image',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])],
                              blank=True)
    status = models.CharField(max_length=15, choices=STATUSES, default=STATUSES[0][0], verbose_name='Статус')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title
