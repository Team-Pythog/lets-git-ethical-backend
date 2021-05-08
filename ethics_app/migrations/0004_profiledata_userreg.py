# Generated by Django 3.2.1 on 2021-05-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethics_app', '0003_alter_dilemmas_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('user_thumbnail', models.TextField()),
                ('user_header', models.TextField()),
                ('bio', models.TextField()),
                ('gender', models.CharField(max_length=32)),
                ('instagram', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=128)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
