# Generated by Django 2.0.2 on 2018-04-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtasks', '0005_auto_20180418_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='feedback',
        ),
        migrations.AddField(
            model_name='task',
            name='resolution',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='resolution'),
        ),
    ]