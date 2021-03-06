# Generated by Django 2.1.1 on 2018-09-17 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='ItemContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_cd', models.CharField(max_length=2)),
                ('field_name', models.CharField(max_length=200)),
                ('field_value', models.CharField(max_length=200)),
                ('calendar_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atriacalendar.CalendarItem')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_description', models.CharField(max_length=200)),
                ('item_start_date', models.DateTimeField(verbose_name='start date/time')),
                ('item_end_date', models.DateTimeField(verbose_name='end date/time')),
                ('calendar_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atriacalendar.CalendarItem')),
            ],
        ),
    ]
