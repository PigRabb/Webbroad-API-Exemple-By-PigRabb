# Generated by Django 3.0.6 on 2020-06-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
