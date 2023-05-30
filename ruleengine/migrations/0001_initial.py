# Generated by Django 4.2 on 2023-05-30 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericRules',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('rule_des', models.CharField(max_length=200)),
                ('left_atr', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=10)),
                ('right_atr', models.CharField(max_length=100)),
                ('rule_string', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=200)),
                ('rule_string', models.CharField(max_length=200)),
            ],
        ),
    ]