# Generated by Django 2.0.2 on 2018-02-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180221_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='romans_lesson',
            name='iden',
            field=models.IntegerField(null=True),
        ),
    ]
