# Generated by Django 3.2.3 on 2021-05-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videodata',
            name='vid_id',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
