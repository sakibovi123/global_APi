# Generated by Django 3.1.7 on 2021-04-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.AddField(
            model_name='product',
            name='related_product',
            field=models.BooleanField(default=False),
        ),
    ]
