<<<<<<< HEAD
# Generated by Django 4.2.7 on 2023-12-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='Car_Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
=======
# Generated by Django 4.2.7 on 2023-12-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='car',
            name='Car_Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
>>>>>>> 1536a79ed4bb132d457adca7cd486953d8e04534
