# Generated by Django 3.0.6 on 2020-05-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='sort_order',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]