# Generated by Django 3.2.9 on 2021-12-19 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_genre_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre_music', to='music.genre'),
        ),
    ]
