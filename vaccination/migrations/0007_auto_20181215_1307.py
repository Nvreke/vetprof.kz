# Generated by Django 2.1.3 on 2018-12-15 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0006_auto_20181209_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccination',
            name='bloodtest',
            field=models.ForeignKey(blank=True, help_text='Тест крови', null=True, on_delete=django.db.models.deletion.CASCADE, to='vaccination.Bloodtest', verbose_name='Тест крови'),
        ),
    ]
