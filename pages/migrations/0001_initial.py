# Generated by Django 5.0.2 on 2024-03-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('google_plus_link', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]