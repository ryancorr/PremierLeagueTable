# Generated by Django 3.1.3 on 2020-11-21 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0022_auto_20201119_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='teams',
        ),
        migrations.AlterField(
            model_name='game',
            name='teamone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teamone', to='table.team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='teamtwo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teamtwo', to='table.team'),
        ),
    ]