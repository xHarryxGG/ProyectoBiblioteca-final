# Generated by Django 4.2.7 on 2023-12-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academico',
            name='prestamos',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='administrativo',
            name='prestamos',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='prestamos',
            field=models.CharField(default=0, max_length=6),
        ),
    ]
