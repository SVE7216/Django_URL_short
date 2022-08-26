# Generated by Django 3.1 on 2022-08-25 13:04

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
            name='URLModels',
            fields=[
                ('origin_url', models.URLField()),
                ('short_id', models.SlugField(max_length=8, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
                'ordering': ['-date'],
            },
        ),
    ]
