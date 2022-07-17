# Generated by Django 4.0.3 on 2022-07-17 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rootapp', '0002_instation'),
        ('controller', '0006_remove_admin_instation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='instation_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rootapp.instation'),
        ),
    ]