# Generated by Django 3.1.3 on 2020-11-19 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0021_auto_20201119_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='table.team'),
        ),
    ]