# Generated by Django 3.1.6 on 2021-02-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210219_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Image_Credit',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]