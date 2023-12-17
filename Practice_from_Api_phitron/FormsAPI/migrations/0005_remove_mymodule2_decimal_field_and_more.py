# Generated by Django 4.2.7 on 2023-12-12 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormsAPI', '0004_mymodule2_file_path_field_mymodule2_float_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodule2',
            name='decimal_field',
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='generic_ip_address_field',
            field=models.GenericIPAddressField(default=14),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='integer_field',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='many_to_many_field',
            field=models.ManyToManyField(to='FormsAPI.mymodule1'),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='positive_big_integer_field',
            field=models.PositiveBigIntegerField(default=14),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='positive_small_integer_field',
            field=models.PositiveSmallIntegerField(default=30),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='small_integer_field',
            field=models.SmallIntegerField(default=14),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='text_field',
            field=models.TextField(default='kmal'),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='time_field',
            field=models.TimeField(default=datetime.datetime(2023, 12, 12, 14, 43, 2, 406682)),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='url_field',
            field=models.URLField(default='http://google.ocm'),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='uuid_field',
            field=models.UUIDField(default='aaakddkdk34'),
        ),
    ]
