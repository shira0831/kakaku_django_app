# Generated by Django 4.0.4 on 2022-04-25 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakaku_django_app', '0012_sp_製品名'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpc',
            name='OS種類',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
