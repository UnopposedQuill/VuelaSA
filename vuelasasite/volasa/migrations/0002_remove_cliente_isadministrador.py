# Generated by Django 2.1.3 on 2018-11-10 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volasa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='isAdministrador',
        ),
    ]