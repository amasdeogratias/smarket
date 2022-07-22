# Generated by Django 3.2.13 on 2022-07-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductId', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Code', models.CharField(max_length=200, null=True)),
                ('Group', models.CharField(max_length=200, null=True)),
                ('MainGroup', models.CharField(max_length=200, null=True)),
                ('Unit', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
