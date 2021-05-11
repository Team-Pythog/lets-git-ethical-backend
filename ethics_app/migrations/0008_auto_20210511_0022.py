# Generated by Django 3.2.1 on 2021-05-11 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethics_app', '0007_delete_userreg'),
    ]

    operations = [
        migrations.AddField(
            model_name='dilemmas',
            name='optionA',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='dilemmas',
            name='optionB',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='dilemmas',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]