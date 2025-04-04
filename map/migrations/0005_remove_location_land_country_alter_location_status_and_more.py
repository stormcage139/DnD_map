# Generated by Django 5.1.2 on 2025-03-09 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_location_land_location_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='Land',
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='map.location')),
            ],
            bases=('map.location',),
        ),
        migrations.AlterField(
            model_name='location',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='map.location')),
                ('Land', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.country')),
            ],
            bases=('map.location',),
        ),
        migrations.CreateModel(
            name='Vilage',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='map.location')),
                ('Land', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.country')),
            ],
            bases=('map.location',),
        ),
    ]
