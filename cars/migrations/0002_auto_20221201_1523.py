# Generated by Django 3.2.16 on 2022-12-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='milage',
            new_name='mileage',
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_rb5ucj', upload_to='images/'),
        ),
    ]