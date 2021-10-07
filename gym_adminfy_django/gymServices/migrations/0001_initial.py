# Generated by Django 3.2 on 2021-05-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('description', models.CharField(db_column='Description', max_length=80)),
                ('hourfee', models.DecimalField(db_column='HourFee', decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'Service',
                'managed': True,
            },
        ),
    ]
