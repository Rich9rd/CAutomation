# Generated by Django 3.2.4 on 2021-08-25 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning', '0002_alter_user_truck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
