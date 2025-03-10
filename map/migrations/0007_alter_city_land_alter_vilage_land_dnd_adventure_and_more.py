# Generated by Django 5.1.2 on 2025-03-10 08:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_location_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='Land',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to='map.country'),
        ),
        migrations.AlterField(
            model_name='vilage',
            name='Land',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='villages', to='map.country'),
        ),
        migrations.CreateModel(
            name='Dnd_adventure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('heroes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hero_m',
            name='adventures',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.dnd_adventure', verbose_name='heroes'),
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('adventures', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.dnd_adventure', verbose_name='heroes')),
            ],
        ),
        migrations.AddField(
            model_name='dnd_adventure',
            name='npcs',
            field=models.ManyToManyField(to='map.npc'),
        ),
        migrations.AddField(
            model_name='location',
            name='npsc',
            field=models.ManyToManyField(to='map.npc', verbose_name='where_was'),
        ),
    ]
