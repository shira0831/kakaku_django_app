# Generated by Django 4.0.4 on 2022-04-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakaku_django_app', '0021_alter_usedpc_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedpc',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
