# Generated by Django 3.1 on 2020-08-26 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='age',
        ),
        migrations.AddField(
            model_name='myuser',
            name='displayname',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]