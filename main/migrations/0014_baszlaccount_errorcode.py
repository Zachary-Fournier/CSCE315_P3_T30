# Generated by Django 3.2.9 on 2021-12-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_imagefile'),
    ]

    operations = [
        migrations.AddField(
            model_name='baszlaccount',
            name='errorCode',
            field=models.TextField(blank=True, null=True),
        ),
    ]