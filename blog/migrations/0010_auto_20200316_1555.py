# Generated by Django 3.0.3 on 2020-03-16 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200316_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='datatime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 7, 55, 42, 777399, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 7, 55, 42, 774753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sale',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 7, 55, 42, 775583, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 7, 55, 42, 743831, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vendorsaleinvoice',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 7, 55, 42, 776127, tzinfo=utc)),
        ),
    ]
