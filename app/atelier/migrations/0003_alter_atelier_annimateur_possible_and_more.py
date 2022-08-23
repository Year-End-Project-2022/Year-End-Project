# Generated by Django 4.0.5 on 2022-08-23 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('atelier', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='annimateur_possible',
            field=models.ManyToManyField(blank=True, help_text='liste des personnes capable de faire le cour', related_name='annimateur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='presonne_interesse',
            field=models.ManyToManyField(blank=True, help_text='liste des personnes intéressées', related_name='interresse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='session',
            name='seance',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='atelier.seance'),
        ),
    ]
