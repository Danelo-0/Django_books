# Generated by Django 5.0 on 2023-12-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dateBirth',
            field=models.DateField(auto_now=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='dateDeath',
            field=models.DateField(auto_now=True, verbose_name='Дата смерти'),
        ),
    ]
