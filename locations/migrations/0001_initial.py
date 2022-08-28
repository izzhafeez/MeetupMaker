# Generated by Django 3.1 on 2022-08-28 04:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=8, max_digits=9, validators=[django.core.validators.MinValueValidator(1.23776), django.core.validators.MaxValueValidator(1.47066)])),
                ('lon', models.DecimalField(decimal_places=8, max_digits=11, validators=[django.core.validators.MinValueValidator(103.61751), django.core.validators.MaxValueValidator(104.0436)])),
            ],
        ),
        migrations.CreateModel(
            name='Halal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.coordinates')),
            ],
        ),
        migrations.CreateModel(
            name='Mall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('stores', models.IntegerField(default=0)),
                ('desirability', models.DecimalField(decimal_places=4, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.coordinates')),
                ('halals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.halal')),
            ],
        ),
        migrations.CreateModel(
            name='MRT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('desirability', models.DecimalField(decimal_places=4, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.coordinates')),
                ('malls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.mall')),
            ],
        ),
    ]