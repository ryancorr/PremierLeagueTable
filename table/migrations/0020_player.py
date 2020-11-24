# Generated by Django 3.1.3 on 2020-11-19 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0019_club_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('number', models.IntegerField(null=True)),
                ('position', models.CharField(max_length=10, null=True)),
                ('nation', models.CharField(max_length=30, null=True)),
                ('picture', models.CharField(max_length=200, null=True)),
                ('squad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.club')),
            ],
        ),
    ]