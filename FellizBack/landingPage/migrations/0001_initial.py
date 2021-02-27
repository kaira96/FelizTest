# Generated by Django 3.1.7 on 2021-02-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCoffe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('reviews', models.TextField()),
            ],
        ),
    ]