# Generated by Django 4.0.3 on 2022-07-02 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rootapp', '0011_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='teacher-profile-image/')),
                ('teacher_id', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=14)),
                ('email_address', models.CharField(max_length=30)),
                ('present_address', models.TextField(max_length=1000)),
                ('permanent_address', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=15)),
                ('payment_in_date', models.DateField()),
                ('payment_amount', models.CharField(max_length=100000)),
                ('payment_month', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rootapp.month')),
            ],
        ),
    ]
