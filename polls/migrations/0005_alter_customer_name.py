# Generated by Django 5.0.4 on 2024-07-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
