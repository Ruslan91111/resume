# Generated by Django 4.1.3 on 2022-12-21 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_remove_rating_star_rating_rating_alter_rating_movie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movies', verbose_name='фильм')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Рейтинг фильма',
                'verbose_name_plural': 'Рейтинги фильма',
            },
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
