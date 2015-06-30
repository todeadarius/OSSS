# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150627_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='vote',
        ),
        migrations.AlterField(
            model_name='vote',
            name='name',
            field=models.ForeignKey(to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='score',
            name='vote',
            field=models.ForeignKey(to='movies.Vote'),
        ),
    ]
