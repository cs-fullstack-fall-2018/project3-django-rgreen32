# Generated by Django 2.0.6 on 2018-10-26 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widthdrawl', models.IntegerField(default=0)),
                ('widthdrawl_date', models.DateTimeField(verbose_name='date published')),
                ('deposit', models.IntegerField(default=0)),
                ('deposit_date', models.DateTimeField(verbose_name='date published')),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Account')),
            ],
        ),
    ]
