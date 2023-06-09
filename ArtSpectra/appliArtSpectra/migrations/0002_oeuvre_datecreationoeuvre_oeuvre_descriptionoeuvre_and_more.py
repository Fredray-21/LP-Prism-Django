# Generated by Django 4.2.1 on 2023-05-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliArtSpectra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oeuvre',
            name='dateCreationOeuvre',
            field=models.DateField(default='1900-01-01', verbose_name="Date de création de l'oeuvre"),
        ),
        migrations.AddField(
            model_name='oeuvre',
            name='descriptionOeuvre',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name="Description de l'oeuvre"),
        ),
        migrations.AddField(
            model_name='oeuvre',
            name='dimensionOeuvre',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name="Dimension de l'oeuvre"),
        ),
        migrations.AlterField(
            model_name='oeuvre',
            name='nomOeuvre',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name="Nom de l'oeuvre"),
        ),
    ]
