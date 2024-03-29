# Generated by Django 4.0.5 on 2022-07-04 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atelier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publier', models.BooleanField(default=False)),
                ('titre', models.CharField(help_text="titre de l'atelier", max_length=200)),
                ('image', models.ImageField(help_text="image principale de l'atelier", null=True, upload_to='static/img/atelier/principale')),
                ('miniature', models.ImageField(help_text="image de la liste d'atelier", null=True, upload_to='static/img/atelier/miniatures')),
                ('objectif', models.TextField(help_text="description global de l'atelier")),
                ('point_abordes', models.TextField(help_text="liste des points importants de l'atelier\n                    (retour a la ligne pour les '-')")),
                ('nb_seance_distance', models.IntegerField(default=0, help_text='nombre de séance pouvant être faite a distance\n            (uniquement informatique)\n            les séance a distance peuvent\n            être quand même fait en présentiel')),
                ('nb_seance_physique', models.IntegerField(default=0, help_text="nombre de séance qui ne peuvent que être faite sur place\n        (besoins d'une machine sur place)")),
                ('minimum_inscrit', models.IntegerField(default=0, help_text='nombre de personnes minimum')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='date de la séance')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atelier', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atelier.atelier')),
                ('dates', models.OneToOneField(blank=True, default=django.db.models.deletion.SET_NULL, help_text='date des séances', null=True, on_delete=django.db.models.deletion.SET_NULL, to='atelier.session')),
            ],
        ),
    ]
