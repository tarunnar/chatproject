# Generated by Django 3.2.12 on 2022-02-27 10:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField()),
                ('is_sent', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 2, 27, 10, 41, 45, 994248, tzinfo=utc))),
            ],
        ),
    ]
