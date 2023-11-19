# Generated by Django 4.2.7 on 2023-11-19 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('post_code', models.IntegerField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='adress',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.address'),
        ),
    ]
