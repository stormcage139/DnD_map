# Generated by Django 5.1.2 on 2025-03-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0018_alter_dnd_adventure_options_alter_location_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dnd_adventure',
            options={'ordering': ['number'], 'verbose_name': 'Приключение', 'verbose_name_plural': 'Приключения'},
        ),
        migrations.AlterField(
            model_name='dnd_adventure',
            name='number',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=1000, null=True, verbose_name='Номер приключения'),
        ),
    ]
