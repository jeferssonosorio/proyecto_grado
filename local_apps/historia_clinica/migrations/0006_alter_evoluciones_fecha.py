# Generated by Django 3.2.9 on 2021-11-22 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("historia_clinica", "0005_alter_evoluciones_fecha"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evoluciones",
            name="fecha",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
