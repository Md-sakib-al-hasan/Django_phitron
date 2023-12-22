# Generated by Django 4.2.7 on 2023-12-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormsAPI', '0003_mymodule2_decimal_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodule2',
            name='file_path_field',
            field=models.FilePathField(default='FormsAPI/forms.html', path='./templates/FormsAPI'),
        ),
        migrations.AddField(
            model_name='mymodule2',
            name='float_field',
            field=models.FloatField(default=3.5),
        ),
    ]