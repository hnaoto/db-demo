# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo', '0011_auto_20161201_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pointScored', models.IntegerField(default=0)),
                ('passYards', models.IntegerField(default=0)),
                ('rushYards', models.IntegerField(default=0)),
                ('recYards', models.IntegerField(default=0)),
                ('rushTDs', models.IntegerField(default=0)),
                ('recTDs', models.IntegerField(default=0)),
                ('interceptions', models.IntegerField(default=0)),
                ('fumblesLost', models.IntegerField(default=0)),
                ('twoPtConversion', models.IntegerField(default=0)),
                ('passTDs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Consistency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(default=0)),
                ('eliteScore', models.FloatField(default=0)),
                ('topScore', models.FloatField(default=0)),
                ('subparScore', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ir', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=5)),
                ('dfy', models.BooleanField(default=False)),
                ('injuryName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kicker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fg', models.IntegerField(default=0)),
                ('fga', models.IntegerField(default=0)),
                ('xpa', models.IntegerField(default=0)),
                ('xp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('espnRank', models.IntegerField(default=-1)),
                ('nflRank', models.IntegerField(default=-1)),
                ('sugPos', models.CharField(max_length=3, choices=[(b'QB', b'Quater Back'), (b'RB', b'Running Back'), (b'WR', b'Wide Receiver'), (b'TE', b'Tight End'), (b'KI', b'Kicker'), (b'DE', b'Defense')])),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('experience', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=2, choices=[(b'QB', b'Quater Back'), (b'RB', b'Running Back'), (b'WR', b'Wide Receiver'), (b'TE', b'Tight End'), (b'KI', b'Kicker'), (b'DE', b'Defense')])),
            ],
        ),
        migrations.CreateModel(
            name='SeasonOffensiveStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pointScored', models.IntegerField(default=0)),
                ('passYards', models.IntegerField(default=0)),
                ('rushYards', models.IntegerField(default=0)),
                ('recYards', models.IntegerField(default=0)),
                ('rushTDs', models.IntegerField(default=0)),
                ('recTDs', models.IntegerField(default=0)),
                ('interceptions', models.IntegerField(default=0)),
                ('fumblesLost', models.IntegerField(default=0)),
                ('twoPtConversion', models.IntegerField(default=0)),
                ('passTDs', models.IntegerField(default=0)),
                ('pid', models.ForeignKey(to='dbdemo.Players')),
            ],
        ),
        migrations.CreateModel(
            name='Suspended',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reasons', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=5)),
                ('susLength', models.IntegerField(default=0)),
                ('dfy', models.BooleanField(default=False)),
                ('pid', models.ForeignKey(to='dbdemo.Players')),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayerRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.ForeignKey(to='dbdemo.Players')),
                ('teamId', models.ForeignKey(to='dbdemo.Team')),
            ],
        ),
        migrations.AddField(
            model_name='playerrank',
            name='pid',
            field=models.ForeignKey(to='dbdemo.Players'),
        ),
        migrations.AddField(
            model_name='kicker',
            name='pid',
            field=models.ForeignKey(to='dbdemo.Players'),
        ),
        migrations.AddField(
            model_name='injury',
            name='pid',
            field=models.ForeignKey(to='dbdemo.Players'),
        ),
        migrations.AddField(
            model_name='consistency',
            name='pid',
            field=models.ForeignKey(to='dbdemo.Players', null=True),
        ),
        migrations.AddField(
            model_name='careerstats',
            name='pid',
            field=models.ForeignKey(to='dbdemo.Players'),
        ),
    ]
