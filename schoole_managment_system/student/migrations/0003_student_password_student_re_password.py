# Generated by Django 4.0.3 on 2022-07-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_password_remove_student_re_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='re_password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
