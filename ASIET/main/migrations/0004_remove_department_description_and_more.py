# Generated by Django 5.2.2 on 2025-06-16 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_aboutus_image_department_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='description',
        ),
        migrations.RemoveField(
            model_name='department',
            name='image',
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
