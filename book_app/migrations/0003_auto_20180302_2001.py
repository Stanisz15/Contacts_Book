# Generated by Django 2.0.2 on 2018-03-02 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_auto_20180302_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book_app.Person'),
            preserve_default=False,
        ),
    ]