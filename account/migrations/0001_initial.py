# Generated by Django 3.2.1 on 2021-05-14 11:53

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(default=-1, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/profile')),
                ('header', models.CharField(max_length=64)),
                ('bio', models.CharField(blank=True, max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
