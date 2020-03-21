# Generated by Django 3.0.4 on 2020-03-21 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('hashtag', models.TextField(max_length=279, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('type_stat', models.CharField(max_length=7, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('realname', models.CharField(max_length=25)),
                ('following', models.PositiveIntegerField()),
                ('followers', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id_tweet', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField(help_text='280 characters max', max_length=280)),
                ('hashtag_in_tweet', models.ManyToManyField(related_name='hashtags_tweet', to='twitter.Hashtag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.TwitterUser')),
            ],
        ),
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_value', models.PositiveIntegerField()),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.Statistics')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.Tweet')),
            ],
        ),
    ]
