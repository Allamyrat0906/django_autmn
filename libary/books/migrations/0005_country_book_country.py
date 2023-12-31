# Generated by Django 4.2.7 on 2023-11-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_address_book_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_c', models.CharField(max_length=100)),
                ('short_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='country',
            field=models.ManyToManyField(to='books.country'),
        ),
    ]
