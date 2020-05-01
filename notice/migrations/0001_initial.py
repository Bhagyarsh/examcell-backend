# Generated by Django 3.0.5 on 2020-05-01 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('uploadedatetime', models.DateTimeField(auto_now_add=True)),
                ('displaytill', models.DateField()),
                ('noticeText', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('displaytoall', models.BooleanField(default=False)),
                ('displaytoparents', models.BooleanField(default=False)),
                ('displaytoclasses', models.ManyToManyField(to='academic.klass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.collegestaff')),
            ],
        ),
    ]
