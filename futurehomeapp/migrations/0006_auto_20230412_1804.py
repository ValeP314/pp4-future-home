# Generated by Django 3.2.18 on 2023-04-12 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futurehomeapp', '0005_auto_20230408_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='futurehomeapp.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='futurehomeapp.listing'),
        ),
    ]
