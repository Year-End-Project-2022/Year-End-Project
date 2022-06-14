# Generated by Django 4.0.5 on 2022-06-14 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGalerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('alt', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='static/img/galerie')),
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
            name='PersonneDispo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
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
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Atelier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(help_text="titre de l'atelier", max_length=200)),
                ('image', models.ImageField(help_text="image principale de l'atelier", null=True, upload_to='static/img/atelier/principale')),
                ('miniature', models.ImageField(help_text="image de la liste d'atelier", null=True, upload_to='static/img/atelier/miniatures')),
                ('objectif', models.TextField(help_text="description global de l'atelier")),
                ('point_abordes', models.TextField(help_text="liste des points importants de l'atelier (retour a la ligne pour les '-')")),
                ('nb_seance_distance', models.IntegerField(default=0, help_text='nombre de séance pouvant être faite a distance\n            (uniquement informatique)\n            les séance a distance peuvent être quand même fait en présentiel')),
                ('nb_seance_physique', models.IntegerField(default=0, help_text="nombre de séance qui ne peuvent que être faite sur place\n        (besoins d'une machine sur place)")),
                ('annimateur_possible', models.ManyToManyField(help_text='liste des personnes capable de faire le cour   ', to='site_web.personnedispo')),
                ('niveau', models.ForeignKey(help_text="Niveau de difficulté de l'atelier", on_delete=django.db.models.deletion.PROTECT, to='site_web.niveau')),
                ('publique', models.ForeignKey(help_text='type de publics pouvant être intéressé', on_delete=django.db.models.deletion.PROTECT, to='site_web.publique')),
                ('theme', models.ForeignKey(help_text="theme de l'atelier (ex: Modélisation, Programmation...)", on_delete=django.db.models.deletion.PROTECT, to='site_web.theme')),
            ],
        ),
    ]
