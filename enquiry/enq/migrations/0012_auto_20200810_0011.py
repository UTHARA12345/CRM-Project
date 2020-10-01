# Generated by Django 3.0.6 on 2020-08-09 18:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enq', '0011_auto_20200724_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='student_name',
            field=models.CharField(default=None, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='coursefee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='enq.Admission'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='student_name',
            field=models.CharField(default=None, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admission',
            name='date',
            field=models.DateField(default=datetime.date(2020, 8, 10)),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry_date',
            field=models.DateField(default=datetime.date(2020, 8, 10)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(default=datetime.date(2020, 8, 10)),
        ),
    ]
