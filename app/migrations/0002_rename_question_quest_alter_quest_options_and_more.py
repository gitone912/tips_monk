# Generated by Django 4.1.5 on 2023-01-18 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='question',
            new_name='quest',
        ),
        migrations.AlterModelOptions(
            name='quest',
            options={},
        ),
        migrations.AlterModelTable(
            name='quest',
            table=None,
        ),
    ]