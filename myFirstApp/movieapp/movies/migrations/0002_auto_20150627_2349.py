# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='vote',
        ),
        migrations.AddField(
            model_name='movie',
            name='vote',
            field=models.ForeignKey(default=0, to='movies.Vote'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vote',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
