# Generated by Django 2.1.2 on 2018-11-11 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0011_auto_20181111_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 11, 11, 8, 28, 27, 216484, tzinfo=utc)),
        ),
    ]