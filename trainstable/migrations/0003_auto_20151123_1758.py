# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainstable', '0002_auto_20151123_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='station_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='train',
            name='train_id',
            field=models.IntegerField(default=0),
        ),
    ]
