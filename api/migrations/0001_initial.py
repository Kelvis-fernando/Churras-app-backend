# Generated by Django 5.0.1 on 2024-01-23 17:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Churras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=165)),
                ('image', models.ImageField(upload_to='churras_images/')),
                ('address', models.CharField(max_length=165)),
                ('items', models.JSONField()),
                ('participantes', models.ManyToManyField(related_name='churras_participations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
