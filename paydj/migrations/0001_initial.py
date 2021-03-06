# Generated by Django 3.2.5 on 2021-07-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=500)),
                ('desc', models.CharField(default='', max_length=5000)),
                ('email', models.CharField(default='', max_length=500)),
                ('phone', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Paymentt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('payment_id', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
