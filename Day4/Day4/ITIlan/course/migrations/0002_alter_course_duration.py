# Generated by Django 5.1.7 on 2025-03-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
