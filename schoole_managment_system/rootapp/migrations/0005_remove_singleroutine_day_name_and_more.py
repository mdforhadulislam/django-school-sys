# Generated by Django 4.0.3 on 2022-07-02 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_remove_studentroutine_day'),
        ('rootapp', '0004_remove_singleroutine_class_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singleroutine',
            name='day_name',
        ),
        migrations.RemoveField(
            model_name='subjectname',
            name='class_number',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='SingleRoutine',
        ),
        migrations.DeleteModel(
            name='SubjectName',
        ),
    ]
