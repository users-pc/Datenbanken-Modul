# Generated by Django 5.0.6 on 2024-06-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bevölkerung',
            name='dg',
            field=models.IntegerField(null=True),
        ),
    ]
