# Generated by Django 3.2.5 on 2021-08-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=20)),
                ('Lastname', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=10)),
                ('PhoneNo', models.IntegerField(max_length=10)),
            ],
        ),
    ]
