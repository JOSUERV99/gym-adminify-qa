# Generated by Django 3.2 on 2021-10-07 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdmSchedule', '0001_initial'),
        ('gymSettings', '0002_auto_20211007_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='schedule',
            field=models.ForeignKey(db_column='Schedule_ID', default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='AdmSchedule.schedule'),
        ),
    ]