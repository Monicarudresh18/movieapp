# Generated by Django 3.0.7 on 2020-09-07 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviedetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('releasedate', models.DateField()),
                ('moviename', models.CharField(max_length=50)),
                ('hero', models.CharField(max_length=50)),
                ('heroine', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
