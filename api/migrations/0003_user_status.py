# Generated by Django 3.0.6 on 2020-05-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200529_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
