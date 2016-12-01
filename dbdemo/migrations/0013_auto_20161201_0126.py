# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo', '0012_auto_20161201_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerrank',
            name='sugPos',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.CharField(max_length=3),
        ),
    ]
