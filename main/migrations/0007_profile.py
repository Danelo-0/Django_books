# Generated by Django 5.0 on 2023-12-22 14:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_author_datebirth_alter_author_datedeath'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True, verbose_name='Город')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('lid', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
