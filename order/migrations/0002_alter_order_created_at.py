# Generated by Django 3.2.7 on 2022-05-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]