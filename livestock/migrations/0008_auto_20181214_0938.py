# Generated by Django 2.1.3 on 2018-12-14 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0007_auto_20181209_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestock',
            name='id',
            field=models.CharField(help_text='KZB212345678', max_length=100, primary_key=True, serialize=False, verbose_name='Номер животного'),
        ),
    ]
