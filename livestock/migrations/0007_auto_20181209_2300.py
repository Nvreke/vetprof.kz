# Generated by Django 2.1.3 on 2018-12-09 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0006_auto_20181209_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestock',
            name='typeoflivestock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.TypesofLiveStock', verbose_name='Тип Животного'),
        ),
    ]
