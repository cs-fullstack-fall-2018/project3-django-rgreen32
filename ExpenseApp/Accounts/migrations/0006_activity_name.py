# Generated by Django 2.0.6 on 2018-10-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_auto_20181029_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]