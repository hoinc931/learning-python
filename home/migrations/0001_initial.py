# Generated by Django 4.0 on 2021-12-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
