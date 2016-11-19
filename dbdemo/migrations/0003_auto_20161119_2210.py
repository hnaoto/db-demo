# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo', '0002_team_defenseid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='defenseID',
            field=models.ForeignKey(default=-1, to='dbdemo.Defense'),
        ),
    ]
