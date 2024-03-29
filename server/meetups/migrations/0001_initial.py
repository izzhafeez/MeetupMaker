# Generated by Django 3.2.6 on 2023-06-13 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('meetup_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetup_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.meetup')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.person')),
            ],
        ),
    ]
