# Generated by Django 3.0.5 on 2020-04-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
