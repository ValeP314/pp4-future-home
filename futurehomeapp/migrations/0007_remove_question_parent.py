# Generated by Django 3.2.18 on 2023-04-12 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futurehomeapp', '0006_auto_20230412_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='parent',
        ),
    ]
