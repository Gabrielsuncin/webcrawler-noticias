# Generated by Django 2.2 on 2021-03-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_auto_20210318_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='jornal',
            field=models.CharField(max_length=200),
        ),
    ]
