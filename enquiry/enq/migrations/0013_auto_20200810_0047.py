# Generated by Django 3.0.6 on 2020-08-09 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enq', '0012_auto_20200810_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='coursefee',
            new_name='cfee',
        ),
    ]
