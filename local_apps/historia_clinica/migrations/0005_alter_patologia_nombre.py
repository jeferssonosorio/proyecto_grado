# Generated by Django 3.2.9 on 2021-11-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("historia_clinica", "0004_paciente_patologia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patologia",
            name="nombre",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
