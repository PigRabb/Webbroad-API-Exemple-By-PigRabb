# Generated by Django 3.0.6 on 2020-06-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200601_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='content',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='content',
            field=models.CharField(max_length=63206),
        ),
    ]
