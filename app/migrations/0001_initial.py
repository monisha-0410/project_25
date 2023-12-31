# Generated by Django 4.2.6 on 2023-12-10 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('Country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Country_Name', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('Capital_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('capital_name', models.CharField(max_length=100)),
                ('Country_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]
