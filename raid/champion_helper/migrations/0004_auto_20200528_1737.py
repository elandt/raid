# Generated by Django 3.0.6 on 2020-05-28 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champion_helper', '0003_load_champions_20200526_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['type', 'name']},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['location']},
        ),
    ]