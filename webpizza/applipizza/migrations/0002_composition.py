# Generated by Django 4.2 on 2023-04-03 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applipizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('idComposition', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.CharField(max_length=100, verbose_name="Quantité de l'ingrédient")),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applipizza.ingredient')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applipizza.pizza')),
            ],
            options={
                'unique_together': {('ingredient', 'pizza')},
            },
        ),
    ]
