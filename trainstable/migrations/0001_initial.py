# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('station_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_arrive', models.DateTimeField()),
                ('time_depart', models.DateTimeField()),
                ('route', models.IntegerField(default=0)),
                ('number_in_route', models.IntegerField(default=0)),
                ('station', models.ForeignKey(to='trainstable.Station')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seats', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='timetable',
            name='train',
            field=models.ForeignKey(to='trainstable.Train'),
        ),
    ]
