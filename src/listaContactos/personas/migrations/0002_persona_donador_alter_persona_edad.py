# Generated by Django 5.0.6 on 2024-06-09 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(),
        ),
    ]