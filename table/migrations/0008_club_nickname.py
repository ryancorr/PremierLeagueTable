# Generated by Django 3.1.3 on 2020-11-18 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_auto_20201117_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='nickname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]