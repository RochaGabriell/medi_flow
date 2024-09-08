# Generated by Django 5.1 on 2024-09-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymodel',
            name='minimum_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade Mínima'),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade'),
        ),
    ]
