# Generated by Django 4.0.4 on 2022-04-26 07:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kakaku_django_app', '0020_alter_usedpc_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedpc',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
