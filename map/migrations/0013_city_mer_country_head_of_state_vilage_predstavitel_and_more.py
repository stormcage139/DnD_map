# Generated by Django 5.1.2 on 2025-03-10 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_alter_location_population_alter_location_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='mer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.npc', verbose_name='Мэр'),
        ),
        migrations.AddField(
            model_name='country',
            name='head_of_state',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.npc', verbose_name='Правитель'),
        ),
        migrations.AddField(
            model_name='vilage',
            name='predstavitel',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.npc', verbose_name='Правитель'),
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='location_picks/'),
        ),
    ]
