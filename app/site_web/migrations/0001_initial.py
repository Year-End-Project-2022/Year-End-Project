# Generated by Django 3.2.5 on 2021-09-02 20:54

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
                ('titre', models.CharField(max_length=200)),
                ('objectif', models.TextField()),
                ('niveau', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='site_web.niveau')),
                ('publique', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_web.publique')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_web.theme')),
            ],
        ),
    ]
