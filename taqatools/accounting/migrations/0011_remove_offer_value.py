# Generated by Django 4.2.4 on 2023-08-17 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_offer_count_saleinvoice_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='value',
        ),
    ]
