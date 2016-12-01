# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo', '0010_auto_20161201_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='careerstats',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='consistency',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='injury',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='kicker',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='playerrank',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='seasonoffensivestats',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='suspended',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='teamplayerrelation',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='teamplayerrelation',
            name='teamId',
        ),
        migrations.DeleteModel(
            name='CareerStats',
        ),
        migrations.DeleteModel(
            name='Consistency',
        ),
        migrations.DeleteModel(
            name='Injury',
        ),
        migrations.DeleteModel(
            name='Kicker',
        ),
        migrations.DeleteModel(
            name='PlayerRank',
        ),
        migrations.DeleteModel(
            name='Players',
        ),
        migrations.DeleteModel(
            name='SeasonOffensiveStats',
        ),
        migrations.DeleteModel(
            name='Suspended',
        ),
        migrations.DeleteModel(
            name='TeamPlayerRelation',
        ),
    ]
