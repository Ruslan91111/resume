# Generated by Django 4.1.3 on 2022-12-21 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_ratingstar_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='star',
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movies', verbose_name='фильм'),
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
