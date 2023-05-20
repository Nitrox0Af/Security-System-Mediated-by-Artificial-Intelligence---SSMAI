# Generated by Django 4.2.1 on 2023-05-20 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_photo_photo_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.owner'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.guest'),
        ),
    ]
