# Generated by Django 4.2.3 on 2023-07-28 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user',
            new_name='authorUser',
        ),
    ]
