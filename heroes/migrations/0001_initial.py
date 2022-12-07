# Generated by Django 4.1.1 on 2022-12-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='heroes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.TextField(help_text='enter the hero id')),
                ('name', models.CharField(max_length=255)),
                ('attack_type', models.TextField(help_text='enter the hero attack type(melee, ranged)')),
                ('roles', models.TextField(help_text='enter hero role/s')),
            ],
        ),
    ]