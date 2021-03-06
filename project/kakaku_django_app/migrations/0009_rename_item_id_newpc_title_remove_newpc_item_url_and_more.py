# Generated by Django 4.0.4 on 2022-04-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakaku_django_app', '0008_newpc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newpc',
            old_name='item_id',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='newpc',
            name='item_url',
        ),
        migrations.AddField(
            model_name='newpc',
            name='メーカーurl',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='newpc',
            name='商品url',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='newpc',
            name='発売日',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
