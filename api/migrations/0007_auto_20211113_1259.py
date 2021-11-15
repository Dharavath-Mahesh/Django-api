# Generated by Django 3.2.9 on 2021-11-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211113_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartimage',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='50', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='cartimage',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='50', editable=False, null=True),
        ),
    ]
