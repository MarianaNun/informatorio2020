# Generated by Django 3.1 on 2020-08-26 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('contrasena', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=100)),
            ],
        ),
    ]