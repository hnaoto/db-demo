# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='defenseID',
            field=models.ForeignKey(default=-1, to='dbdemo.Defense'),
        ),
    ]
