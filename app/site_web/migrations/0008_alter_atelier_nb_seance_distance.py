# Generated by Django 3.2.5 on 2022-06-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_web', '0007_auto_20210903_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='nb_seance_distance',
            field=models.IntegerField(default=0, help_text='nombre de séance pouvant être faite a distance\n            (uniquement informatique)\n            les séance a distance peuvent être quand même fait en présentiel'),
        ),
    ]
