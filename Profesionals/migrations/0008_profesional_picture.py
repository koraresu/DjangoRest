# Generated by Django 2.1.1 on 2018-09-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profesionals', '0007_auto_20180904_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='picture',
            field=models.FileField(default='', upload_to='uploads/avatar/'),
            preserve_default=False,
        ),
    ]