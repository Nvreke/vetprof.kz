# Generated by Django 2.1.3 on 2018-12-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0004_auto_20181207_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oblast',
            name='id',
            field=models.IntegerField(help_text='Almaty-->id(02)', primary_key=True, serialize=False),
        ),
    ]