# Generated by Django 3.2.9 on 2021-12-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_baszlaccount_errorcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baszlaccount',
            name='errorCode',
            field=models.TextField(default=''),
        ),
    ]
