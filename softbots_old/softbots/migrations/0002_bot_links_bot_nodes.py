# Generated by Django 4.0.5 on 2022-06-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softbots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='links',
            field=models.ManyToManyField(to='softbots.link'),
        ),
        migrations.AddField(
            model_name='bot',
            name='nodes',
            field=models.ManyToManyField(to='softbots.node'),
        ),
    ]
