# Generated by Django 4.2.7 on 2023-11-22 15:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_category_application_image_application_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(blank=True, upload_to='application_image', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])], verbose_name='Изображение'),
        ),
    ]
