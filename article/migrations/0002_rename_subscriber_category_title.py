# Generated by Django 4.1.4 on 2023-01-02 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subscriber',
            new_name='title',
        ),
    ]
