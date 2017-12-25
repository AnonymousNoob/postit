# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SummaryHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('version', models.IntegerField(editable=False)),
                ('text', models.TextField()),
                ('book', models.ForeignKey(to='notes.Book')),
            ],
        ),
        migrations.RemoveField(
            model_name='timelog',
            name='notes',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='TimeLog',
        ),
        migrations.AlterUniqueTogether(
            name='summaryhistory',
            unique_together=set([('version', 'book')]),
        ),
    ]
