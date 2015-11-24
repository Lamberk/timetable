# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainstable', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='number_in_route',
            new_name='position_in_route',
        ),
    ]
