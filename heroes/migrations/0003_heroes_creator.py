# Generated by Django 4.1.1 on 2022-12-07 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('heroes', '0002_heroes_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroes',
            name='creator',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
