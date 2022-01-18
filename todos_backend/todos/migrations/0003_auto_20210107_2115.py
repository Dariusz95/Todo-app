# Generated by Django 3.1.4 on 2021-01-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20210102_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]