# Generated by Django 4.2.3 on 2023-07-17 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_rules', models.TextField(default='', max_length=500)),
                ('title', models.TextField(max_length=100)),
                ('image_url', models.TextField(max_length=500)),
                ('game_atlas_id', models.TextField(default='', max_length=50)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
