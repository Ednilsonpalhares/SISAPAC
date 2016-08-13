# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('matricula', models.IntegerField(verbose_name='Matricula')),
                ('senha', models.CharField(max_length=16, verbose_name='Senha')),
            ],
        ),
        migrations.CreateModel(
            name='Horario_Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekdays', models.CharField(choices=[('ND', 'Não definido'), ('SEG', 'Segunda-Feira'), ('TER', 'Terça-Feira'), ('QUA', 'Quarta-Feira'), ('QUI', 'Quinta-Feira'), ('SEX', 'Sexta-Feira')], default='ND', max_length=25)),
                ('turma', models.CharField(max_length=150, verbose_name='Turma')),
                ('disciplina', models.CharField(max_length=255, verbose_name='Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horarios', models.CharField(choices=[('Vazio', 'Indefinido'), ('1M', '07:00 - 08:30'), ('2M', '08:50 - 10:20'), ('3M', '10:30 - 12:00'), ('1T', '13:00 - 14:30'), ('2T', '14:50 - 16:20'), ('3T', '16:30 - 18:00'), ('1N', '18:00 - 19:50'), ('2N', '20:00 - 22:00')], default='Vazio', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Registro_Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data do registro')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsispac.Horarios')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva_Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data do Registro')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appsispac.Funcionario')),
            ],
            bases=('appsispac.funcionario',),
        ),
        migrations.AddField(
            model_name='reserva_sala',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appsispac.Funcionario'),
        ),
        migrations.AddField(
            model_name='reserva_sala',
            name='horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsispac.Horarios'),
        ),
        migrations.AddField(
            model_name='reserva_sala',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appsispac.Sala'),
        ),
        migrations.AddField(
            model_name='registro_frequencia',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appsispac.Sala'),
        ),
        migrations.AddField(
            model_name='horario_professor',
            name='horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsispac.Horarios'),
        ),
        migrations.AddField(
            model_name='registro_frequencia',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appsispac.Professor'),
        ),
        migrations.AddField(
            model_name='professor',
            name='horario',
            field=models.ManyToManyField(to='appsispac.Horario_Professor'),
        ),
    ]
