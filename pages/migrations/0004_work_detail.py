# Generated by Django 4.2 on 2023-08-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_work_datecreate_work_dateupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='detail',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
