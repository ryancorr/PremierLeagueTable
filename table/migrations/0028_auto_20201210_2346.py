# Generated by Django 3.1.3 on 2020-12-11 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0027_remove_player_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='position2',
            new_name='position',
        ),
    ]
