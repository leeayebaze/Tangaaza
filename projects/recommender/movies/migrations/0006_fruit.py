# Generated by Django 2.1.7 on 2019-03-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]