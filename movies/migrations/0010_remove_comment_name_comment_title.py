# Generated by Django 4.1.3 on 2022-12-11 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок комментария'),
        ),
    ]
