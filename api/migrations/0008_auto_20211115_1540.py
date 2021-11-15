# Generated by Django 3.2.9 on 2021-11-15 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20211113_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartimage',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='cartimage',
            name='image_width',
        ),
        migrations.AddField(
            model_name='cartimage',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='api.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartimage',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]