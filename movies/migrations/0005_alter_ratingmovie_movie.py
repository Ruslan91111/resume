# Generated by Django 4.1.3 on 2022-12-21 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_ratingmovie_delete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies', verbose_name='фильм'),
        ),
    ]
