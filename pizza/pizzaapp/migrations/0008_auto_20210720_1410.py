# Generated by Django 3.2.3 on 2021-07-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0007_auto_20210720_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzamodel',
            name='amount',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
