# Generated by Django 4.2.4 on 2023-08-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_alter_purchaseinvoice_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='value',
            field=models.FloatField(),
        ),
    ]
