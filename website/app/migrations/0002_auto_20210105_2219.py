# Generated by Django 3.1.5 on 2021-01-05 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_id',
            field=models.IntegerField(default=0),
        ),
    ]
