# Generated by Django 3.2.5 on 2021-08-07 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(unique=True, upload_to='static/img/outils')),
            ],
        ),
        migrations.CreateModel(
            name='Outils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('type', models.CharField(max_length=200)),
                ('taille', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('marque', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('nombre', models.IntegerField(blank=True, default=1)),
                ('nombre_hs', models.IntegerField(blank=True, default=0)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('categories', models.ManyToManyField(to='formulaire_outils.Categories')),
                ('groupe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='formulaire_outils.groupe')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imageBase', to='formulaire_outils.media')),
                ('image_cote', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='imageCote', to='formulaire_outils.media')),
            ],
        ),
    ]