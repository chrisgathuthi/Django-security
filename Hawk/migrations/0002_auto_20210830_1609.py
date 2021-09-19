# Generated by Django 3.2.4 on 2021-08-30 13:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Hawk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='leave_time',
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='student_image',
        ),
        migrations.AddField(
            model_name='user_data',
            name='qr_code',
            field=models.ImageField(default=datetime.datetime(2021, 8, 30, 13, 9, 45, 556121, tzinfo=utc), help_text='student image', upload_to='qr_codes'),
            preserve_default=False,
        ),
    ]
