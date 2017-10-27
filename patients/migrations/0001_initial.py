# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_history', models.TextField(blank=True, max_length=500)),
                ('family_history', models.TextField(blank=True, max_length=500)),
                ('current_illness', models.TextField(blank=True, max_length=500)),
                ('symptoms', models.TextField(blank=True, max_length=500)),
                ('rehab_diagnose', models.TextField(blank=True, max_length=1000)),
                ('short_term_goals', models.TextField(blank=True, max_length=1000)),
                ('long_term_goals', models.TextField(blank=True, max_length=1000)),
                ('form_filled_by', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('cedula', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('cellphone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('cedula', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=255)),
                ('datebirth', models.DateField()),
                ('refered_by', models.CharField(max_length=255)),
                ('insurance', models.CharField(choices=[('1', 'ARS Humano'), ('2', 'ARS Palic'), ('3', 'SeNaSa'), ('4', 'ARS Banreservas')], max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone_1', models.CharField(blank=True, max_length=255)),
                ('phone_2', models.CharField(blank=True, max_length=255)),
                ('cellphone', models.CharField(blank=True, max_length=255)),
                ('ocupation', models.CharField(blank=True, max_length=255)),
                ('workplace', models.CharField(blank=True, max_length=255)),
                ('position', models.CharField(blank=True, max_length=255)),
                ('work_phone', models.CharField(blank=True, max_length=255)),
                ('emergency_contact', models.CharField(blank=True, max_length=255)),
                ('emergency_phone_1', models.CharField(blank=True, max_length=255)),
                ('emergency_phone_2', models.CharField(blank=True, max_length=255)),
                ('emergency_cellphone', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='clinichistory',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Doctor'),
        ),
        migrations.AddField(
            model_name='clinichistory',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.PatientProfile'),
        ),
    ]
