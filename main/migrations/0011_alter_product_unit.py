# Generated by Django 3.2.13 on 2022-07-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20220728_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Unit',
            field=models.CharField(choices=[('DZ', 'dozen'), ('LT', 'litre'), ('PC', 'piece')], max_length=2, null=True),
        ),
    ]