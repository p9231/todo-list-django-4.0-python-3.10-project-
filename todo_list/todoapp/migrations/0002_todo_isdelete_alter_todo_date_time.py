# Generated by Django 4.0.2 on 2022-03-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isdelete',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_time',
            field=models.CharField(max_length=20),
        ),
    ]