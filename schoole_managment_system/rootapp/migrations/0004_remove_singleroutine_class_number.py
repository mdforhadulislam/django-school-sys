# Generated by Django 4.0.3 on 2022-07-02 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rootapp', '0003_class_rename_title_singleroutine_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singleroutine',
            name='class_number',
        ),
    ]
