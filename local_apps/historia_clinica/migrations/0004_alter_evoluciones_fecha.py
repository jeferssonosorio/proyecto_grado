# Generated by Django 3.2.9 on 2021-11-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("historia_clinica", "0003_auto_20211122_1647"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evoluciones",
            name="fecha",
            field=models.DateField(),
        ),
    ]
