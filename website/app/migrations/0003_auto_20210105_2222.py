# Generated by Django 3.1.5 on 2021-01-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210105_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat_id',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
