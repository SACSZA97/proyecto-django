# Generated by Django 5.0.6 on 2024-06-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnos',
            options={'ordering': ['-created'], 'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AddField(
            model_name='alumnos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografia'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='creado'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='matricula',
            field=models.CharField(max_length=12, verbose_name='Mat'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='turnno',
            field=models.CharField(max_length=10, verbose_name='turno'),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='actualizado'),
        ),
    ]
