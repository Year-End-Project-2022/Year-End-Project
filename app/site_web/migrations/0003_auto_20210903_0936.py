# Generated by Django 3.2.5 on 2021-09-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_web', '0002_auto_20210902_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='atelier',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/atelier/<django.db.models.fields.CharField>'),
        ),
        migrations.AddField(
            model_name='atelier',
            name='miniature',
            field=models.ImageField(null=True, upload_to='static/img/atelier/<django.db.models.fields.CharField>'),
        ),
    ]
