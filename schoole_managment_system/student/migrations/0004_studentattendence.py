# Generated by Django 4.0.3 on 2022-07-01 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=15)),
                ('present_in_date', models.DateField()),
            ],
        ),
    ]
