# Generated by Django 2.2 on 2019-04-28 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('num_count', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
                ('Sexo', models.CharField(max_length=1)),
                ('Edad', models.IntegerField()),
                ('FechaNacimiento', models.DateTimeField()),
                ('Telefono', models.CharField(max_length=10)),
                ('Email', models.TextField()),
                ('Domicilio', models.TextField()),
            ],
        ),
    ]