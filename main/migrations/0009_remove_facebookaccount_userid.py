# Generated by Django 3.2.9 on 2021-12-04 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_facebookaccount_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookaccount',
            name='userID',
        ),
    ]
