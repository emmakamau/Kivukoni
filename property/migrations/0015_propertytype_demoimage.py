# Generated by Django 4.0.2 on 2022-02-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_property_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertytype',
            name='demoimage',
            field=models.ImageField(default=0, upload_to='media'),
        ),
    ]
