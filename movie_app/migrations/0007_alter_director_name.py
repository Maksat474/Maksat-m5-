# Generated by Django 4.2.10 on 2024-03-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_alter_director_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
