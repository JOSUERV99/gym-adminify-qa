# Generated by Django 3.2 on 2021-10-07 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gymPersons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('person', models.OneToOneField(db_column='ID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gymPersons.person')),
                ('balance', models.DecimalField(db_column='Balance', decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'Client',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClientState',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'ClientState',
                'managed': True,
            },
        ),
    ]
