# Generated by Django 2.1.1 on 2018-09-03 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='language_tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profesionals.language')),
            ],
        ),
        migrations.CreateModel(
            name='profesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='profesional_language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profesionals.language')),
                ('profesional_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profesionals.profesional')),
            ],
        ),
    ]