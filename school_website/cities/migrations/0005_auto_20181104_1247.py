# Generated by Django 2.1.2 on 2018-11-04 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_auto_20181104_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
    ]