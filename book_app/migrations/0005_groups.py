# Generated by Django 2.0.2 on 2018-03-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0004_email_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('persons', models.ManyToManyField(to='book_app.Person')),
            ],
        ),
    ]
