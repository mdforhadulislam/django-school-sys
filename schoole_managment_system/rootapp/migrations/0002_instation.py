# Generated by Django 4.0.3 on 2022-07-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rootapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]