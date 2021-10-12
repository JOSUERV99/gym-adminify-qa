# Generated by Django 3.2 on 2021-10-07 23:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gymClients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='clientstate',
            field=models.ForeignKey(db_column='ClientState_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='gymClients.clientstate'),
            preserve_default=False,
        ),
    ]