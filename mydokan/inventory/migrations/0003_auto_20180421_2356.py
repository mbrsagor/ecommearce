# Generated by Django 2.0.4 on 2018-04-21 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='stadus',
            new_name='status',
        ),
    ]