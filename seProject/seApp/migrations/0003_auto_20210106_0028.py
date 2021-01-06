# Generated by Django 3.1.4 on 2021-01-06 00:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seApp', '0002_auto_20210106_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=70, null=True), null=True, size=10),
        ),
        migrations.AddField(
            model_name='clinic',
            name='rating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='time_slots',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(null=True), null=True, size=24),
        ),
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, null=True), null=True, size=1000),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True),
        ),
    ]
