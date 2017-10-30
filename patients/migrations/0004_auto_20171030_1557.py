# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patientprofile_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Fecha de la Terapia', verbose_name='Fecha')),
                ('insurance', models.CharField(choices=[('1', 'ARS Humano'), ('2', 'ARS Palic'), ('3', 'SeNaSa'), ('4', 'ARS Banreservas'), ('5', 'ARS Universal')], max_length=155)),
                ('physiotherapy', models.CharField(blank=True, max_length=2000)),
                ('diagnosis', models.CharField(blank=True, max_length=2000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Doctor')),
            ],
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='insurance',
            field=models.CharField(choices=[('1', 'ARS Humano'), ('2', 'ARS Palic'), ('3', 'SeNaSa'), ('4', 'ARS Banreservas'), ('5', 'ARS Universal')], max_length=255),
        ),
        migrations.AddField(
            model_name='therapy',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.PatientProfile'),
        ),
    ]