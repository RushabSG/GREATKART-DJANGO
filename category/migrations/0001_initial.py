# Generated by Django 3.2.24 on 2024-03-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('category_image', models.ImageField(blank=True, upload_to='photos/categories')),
            ],
        ),
    ]
