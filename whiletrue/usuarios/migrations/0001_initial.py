# Generated by Django 3.1.12 on 2024-12-06 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
            ],
        ),
    ]
