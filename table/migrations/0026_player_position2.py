# Generated by Django 3.1.3 on 2020-12-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0025_team_abrev'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position2',
            field=models.CharField(choices=[('GK', 'Goal Keeper'), ('DF', 'Defender'), ('MF', 'Midfielder'), ('FW', 'Forward')], max_length=10, null=True),
        ),
    ]
