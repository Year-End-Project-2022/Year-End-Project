# Generated by Django 4.0.5 on 2022-07-05 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire_outils', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outils',
            name='image_cote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='imageCote', to='formulaire_outils.media'),
        ),
    ]
