# Generated by Django 4.1.1 on 2022-12-07 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0003_heroes_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heroes',
            name='creator',
        ),
    ]
