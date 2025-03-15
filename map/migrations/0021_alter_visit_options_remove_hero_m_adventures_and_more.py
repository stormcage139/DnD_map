# Generated by Django 5.1.7 on 2025-03-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0020_dnd_adventure_slug_alter_dnd_adventure_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'verbose_name': 'Посещение', 'verbose_name_plural': 'Песещения'},
        ),
        migrations.RemoveField(
            model_name='hero_m',
            name='adventures',
        ),
        migrations.AddField(
            model_name='location',
            name='small_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
