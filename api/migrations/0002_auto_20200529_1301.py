# Generated by Django 3.0.6 on 2020-05-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='post_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
