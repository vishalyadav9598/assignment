# Generated by Django 3.0.5 on 2020-04-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(max_length=11)),
                ('user_id', models.IntegerField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='name', max_length=255)),
            ],
        ),
    ]