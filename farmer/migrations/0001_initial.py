# Generated by Django 2.1.3 on 2018-12-16 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': '1.Страны',
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ИИН')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=40, verbose_name='почта')),
                ('address', models.CharField(max_length=50, verbose_name='Адрес')),
                ('coordinate', models.CharField(blank=True, help_text='Координаты дома(можно посмотреть в google map)', max_length=1000, null=True, verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Фермер',
                'verbose_name_plural': '6.Фермеры',
            },
        ),
        migrations.CreateModel(
            name='Oblast',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер области')),
                ('name', models.CharField(max_length=100, verbose_name='Область')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Country', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': '2.Области',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Регион')),
                ('oblast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Oblast', verbose_name='Область')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': '3.Регионы',
            },
        ),
        migrations.CreateModel(
            name='RuralDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Сельский округ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Сельский округ',
                'verbose_name_plural': '4.Сельские округи',
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Поселок')),
                ('ruraldistrict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.RuralDistrict', verbose_name='Сельский округ')),
            ],
            options={
                'verbose_name': 'Поселки',
                'verbose_name_plural': '5.Поселок',
            },
        ),
        migrations.AddField(
            model_name='farmer',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.Village', verbose_name='Поселок'),
        ),
    ]
