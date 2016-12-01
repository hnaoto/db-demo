# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo', '0007_remove_players_teamid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerrank',
            name='sugPos',
            field=models.CharField(max_length=3, choices=[(b'QB', b'Quater Back'), (b'RB', b'Running Back'), (b'WR', b'Wide Receiver'), (b'TE', b'Tight End'), (b'KI', b'Kicker'), (b'DE', b'Defense')]),
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.CharField(max_length=2, choices=[(b'QB', b'Quater Back'), (b'RB', b'Running Back'), (b'WR', b'Wide Receiver'), (b'TE', b'Tight End'), (b'KI', b'Kicker'), (b'DE', b'Defense')]),
        ),
    ]
