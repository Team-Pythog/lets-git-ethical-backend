# Generated by Django 3.2.1 on 2021-05-13 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethics_app', '0002_alter_dilemmas_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dilemmas',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
