# Generated by Django 4.2.11 on 2024-07-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
