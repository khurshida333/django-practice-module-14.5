# Generated by Django 5.0.6 on 2024-06-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('problem', models.TextField()),
                ('health_condition', models.TextField()),
                ('phone_no', models.CharField(max_length=11)),
            ],
        ),
    ]
