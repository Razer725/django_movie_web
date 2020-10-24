# Generated by Django 3.0.3 on 2020-10-08 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie', verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.RatingStar', verbose_name='Звезда'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie', verbose_name='Фильм'),
        ),
    ]
