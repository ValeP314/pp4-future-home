# Generated by Django 3.2.18 on 2023-04-04 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futurehomeapp', '0002_auto_20230404_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('ber_category', models.TextField()),
                ('price', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'For Sale'), (1, 'Sold')], default=0)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='futurehomeapp.listing')),
            ],
        ),
        migrations.DeleteModel(
            name='Features',
        ),
    ]