# Generated by Django 5.0.6 on 2024-08-13 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job_type', models.CharField(choices=[('email', 'email notification'), ('crunch', 'number crunching')], max_length=50)),
                ('schedule_interval', models.DurationField()),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('next_run', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
