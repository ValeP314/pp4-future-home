# Generated by Django 3.2.18 on 2023-04-08 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futurehomeapp', '0004_auto_20230408_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='ber_category',
            field=models.CharField(max_length=3),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_item', to='futurehomeapp.listing')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
