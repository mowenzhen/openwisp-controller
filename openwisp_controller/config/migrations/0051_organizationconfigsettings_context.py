# Generated by Django 3.2.20 on 2023-07-22 10:49

import collections

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0050_alter_vpnclient_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationconfigsettings',
            name='context',
            field=jsonfield.fields.JSONField(
                blank=True,
                default=dict,
                dump_kwargs={'indent': 4},
                help_text=(
                    'This field can be used to add "Configuration Variables"'
                    ' to the devices.'
                ),
                load_kwargs={'object_pairs_hook': collections.OrderedDict},
                verbose_name='Configuration Variables',
            ),
        ),
    ]
