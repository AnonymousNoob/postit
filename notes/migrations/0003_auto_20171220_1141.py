# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20171220_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('version', models.IntegerField(editable=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Book',
            new_name='Note',
        ),
        migrations.AlterUniqueTogether(
            name='summaryhistory',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='summaryhistory',
            name='book',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='summary',
            new_name='content',
        ),
        migrations.DeleteModel(
            name='SummaryHistory',
        ),
        migrations.AddField(
            model_name='notehistory',
            name='note',
            field=models.ForeignKey(to='notes.Note'),
        ),
        migrations.AlterUniqueTogether(
            name='notehistory',
            unique_together=set([('version', 'note')]),
        ),
    ]
