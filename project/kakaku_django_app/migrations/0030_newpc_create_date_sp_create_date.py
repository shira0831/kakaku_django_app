# Generated by Django 4.0.4 on 2022-04-27 02:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kakaku_django_app', '0029_alter_usedpc_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpc',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='sp',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
