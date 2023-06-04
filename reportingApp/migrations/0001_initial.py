# Generated by Django 4.2.1 on 2023-06-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('timezone_str', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportingApp.store')),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='BusinessHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(0, 'MONDAY'), (1, 'TUESDAY'), (2, 'WEDNESDAY'), (3, 'THURSDAY'), (4, 'FRIDAY'), (5, 'SATURDAY'), (6, 'SUNDAY')])),
                ('start_time_local', models.DateTimeField()),
                ('end_time_local', models.DateTimeField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportingApp.store')),
            ],
        ),
    ]
