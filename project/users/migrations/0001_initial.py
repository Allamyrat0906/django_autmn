# Generated by Django 4.2.7 on 2023-12-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=190)),
                ('age', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=250)),
                ('photo', models.ImageField(upload_to='images')),
                ('country', models.CharField(max_length=100)),
                ('dob', models.DateField(default=None)),
            ],
        ),
    ]