# Generated by Django 4.0.3 on 2022-07-02 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_singleroutine_delete_studentroutine'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]