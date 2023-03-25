# Generated by Django 4.1.7 on 2023-03-24 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('phone', models.IntegerField(verbose_name='Telefono')),
                ('email', models.EmailField(max_length=254, verbose_name='Imagen')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]