# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Defense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pointsAllowed', models.IntegerField(default=0)),
                ('sacks', models.IntegerField(default=0)),
                ('interceptions', models.IntegerField(default=0)),
                ('fumbleRecoveries', models.IntegerField(default=0)),
                ('defTD', models.IntegerField(default=0)),
                ('passRank', models.IntegerField(default=0)),
                ('rushRank', models.IntegerField(default=0)),
                ('puntRetRank', models.IntegerField(default=0)),
                ('kickRetRank', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
