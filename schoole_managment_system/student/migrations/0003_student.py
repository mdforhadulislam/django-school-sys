# Generated by Django 4.0.3 on 2022-07-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentpayment_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='student-profile-image/')),
                ('student_id', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('class_number', models.IntegerField()),
                ('roll_number', models.IntegerField()),
                ('phone_number', models.CharField(max_length=14)),
                ('email_address', models.CharField(max_length=30)),
                ('present_address', models.TextField(max_length=1000)),
                ('permanent_address', models.TextField(max_length=1000)),
            ],
        ),
    ]