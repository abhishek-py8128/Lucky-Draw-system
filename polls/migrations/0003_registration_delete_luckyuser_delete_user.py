# Generated by Django 5.0.4 on 2024-07-11 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_luckyuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('pswd', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='luckyuser',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
