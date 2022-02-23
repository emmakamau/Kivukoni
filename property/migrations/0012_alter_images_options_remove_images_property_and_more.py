# Generated by Django 4.0.2 on 2022-02-22 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_remove_property_image_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.RemoveField(
            model_name='images',
            name='property',
        ),
        migrations.AddField(
            model_name='images',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.images'),
        ),
    ]