# Generated by Django 4.0.2 on 2022-02-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_property_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
    ]