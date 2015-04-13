# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quote', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
    ]
