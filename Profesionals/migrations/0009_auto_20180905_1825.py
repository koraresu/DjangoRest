# Generated by Django 2.1.1 on 2018-09-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profesionals', '0008_profesional_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='uploads/avatar/'),
        ),
    ]