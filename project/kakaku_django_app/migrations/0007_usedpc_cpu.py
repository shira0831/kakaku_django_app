# Generated by Django 4.0.4 on 2022-04-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakaku_django_app', '0006_usedpc_os'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedpc',
            name='CPU',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
