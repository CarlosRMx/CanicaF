# Generated by Django 2.0.13 on 2019-10-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='escrita_por',
            field=models.CharField(default='CANICA', max_length=60),
        ),
        migrations.AddField(
            model_name='noticia',
            name='resumen_notica',
            field=models.TextField(default='...', verbose_name='Breve resumen de la notica'),
        ),
    ]
