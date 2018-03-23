# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _

class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0008_changes_to_psql_jsonfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logentry',
            name='additional_data',
        ),
        migrations.AddField(
            model_name='logentry',
            name='additional_data',
            field=JSONField(null=True, verbose_name=_("additional data"))
        ),
    ]
