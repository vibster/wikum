# Generated by Django 3.0.5 on 2020-04-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0072_auto_20200405_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.CharField(max_length=2000),
        ),
    ]
