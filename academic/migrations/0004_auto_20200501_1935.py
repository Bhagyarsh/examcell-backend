# Generated by Django 3.0.4 on 2020-05-01 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_studenteditprofilerequest_acknowledge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenteditprofilerequest',
            name='enrolledclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.klass'),
        ),
    ]