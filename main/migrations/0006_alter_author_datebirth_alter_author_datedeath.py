# Generated by Django 5.0 on 2023-12-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_author_datebirth_alter_author_datedeath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dateBirth',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='dateDeath',
            field=models.DateField(verbose_name='Дата смерти'),
        ),
    ]
