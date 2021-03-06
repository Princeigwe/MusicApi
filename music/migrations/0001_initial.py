# Generated by Django 3.2.9 on 2021-12-16 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('artiste', models.CharField(max_length=300)),
                ('year', models.DateField()),
                ('cover_photo', models.ImageField(upload_to='covers/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('ROCK', 'Rock'), ('POP MUSIC', 'Pop Music'), ('HIPHOP MUSIC', 'Hip Hop Music'), ('ELECTRONIC DANCE MUSIC', 'Electronic Dance Music'), ('CLASSICAL MUSIC', 'Classical Music'), ('HOUSE MUSIC', 'House Music'), ('TRAP MUSIC', 'Trap Music'), ('JAZZ', 'Jazz')], max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('artiste', models.CharField(max_length=500)),
                ('audio_file', models.FileField(upload_to='audio/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music', to='music.album')),
            ],
            options={
                'verbose_name_plural': 'Music',
            },
        ),
    ]
