# Generated by Django 2.2.5 on 2019-09-07 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catergory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='other', max_length=50)),
                ('image_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('describtion', models.CharField(default='', max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('image_url', models.TextField(null=True)),
                ('prize', models.IntegerField(default=0)),
                ('date', models.DateTimeField(blank=True, default=datetime.date.today)),
                ('alive', models.BooleanField(default=True)),
            ],
        ),
    ]
