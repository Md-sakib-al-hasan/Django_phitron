# Generated by Django 4.2.7 on 2023-12-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=12)),
                ('Instrument_Type', models.CharField(max_length=100)),
            ],
        ),
    ]
